from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from .models import Years, npa, link_npa
from .forms import npa_link_Form
from django.shortcuts import render
# Register your models here.


# Admin Action Functions
def create_link(modeladmin, request, queryset):
  
    form = None
    if 'action' in request.POST:       
           form = npa_link_Form(request.POST)
           if form.is_valid():
               id_npa_s = form.cleaned_data['id_npas']             
               _selected_actio = form.cleaned_data['_selected_action']                            
               select_id_npa_out =  request.POST.get('id_npas', '')
               select_id_pna_sors =_selected_actio.replace("['","")
               select_id_pna_sors = select_id_pna_sors.replace("']","")             
               l = link_npa.objects.create(to_Link_id_npa=select_id_pna_sors, id_npa_id=select_id_npa_out, name=request.POST.get('name', ''))
               l.save()
               
               modeladmin.message_user(request, "связь  %s применена к  документу." % ( id_npa_s ))
               return HttpResponseRedirect(request.get_full_path())

    if not form:
           form = npa_link_Form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
    return render(request, 'admin/test.html', {
                                                'items': queryset,
                                                'form': form, 
                                                'npa':npa.objects.get(pk=request.POST.get('_selected_action')),  
                                                'title':u'создать ссылку'
                                              }
    )

create_link.short_description = u"создать ссылку"


class PhotoAdmin(admin.ModelAdmin):   
    list_display = ( 'nomer','name','vid_del','date')
    ##################################################
    list_filter = ('vid','vid_del', ) 
    ##################################################
    search_fields = ('name', ) 
    ##################################################
    actions = [create_link]    
   

class link_titul(admin.ModelAdmin):
    list_display = ('name', 'id_npa')
    admin.site.site_title = 'Mysite Admin Panel'
    

    
admin.site.register(Years)  
admin.site.register(npa, PhotoAdmin)
admin.site.register(link_npa, link_titul)    

admin.site.site_header= "Администрирование GIS"


