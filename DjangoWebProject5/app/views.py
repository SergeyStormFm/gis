"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Years, npa, link_npa
from array import array

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        { 
            'title':'Home Page',
            'data':datetime.now().year,
            'year':Years.objects.filter(is_active = 1).first(),
            'years':Years.objects.filter(is_active = 1).order_by("name"),
        }
    )
   

def document(request, question_id):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)  
    link1 = ""
    links = link_npa.objects.filter(to_Link_id_npa=question_id).all()   
    for link in links:
        link1 = npa.objects.filter(pk=link.to_Link_id_npa).first()

    x =  link_npa.objects.filter(to_Link_id_npa=question_id).count()   
    y = 4 
   
    
    z=[[0 for row in range(0,x)] for col in range(0,y)]   
         
    count = 0     
    y = 0
    
    for link in links:
        data = npa.objects.filter(pk=link.id_npa_id).first()
        z[0][count]= data.nomer      
        z[1][count]= data.name       
        z[2][count]= data.date
        z[3][count]= data.id
        count += 1
 
    return render(
        request,
        'app/document.html',
        {
            'title':'Contact',
            'npa':npa.objects.get(pk = question_id),
            'year':datetime.now().year,
            'link_ot': link1,
            'link_to': z,
            'count_ot': count,
            
        }
    )
    

def org(request, year_id,vid_id,vid_del_id):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    
    id_ears = Years.objects.filter(name = year_id).first()
    
    return render(
        request,
        'app/org.html',
        {
            'title':'Список документов',
            'vid_del_id':vid_del_id,
            'year_id':year_id,
            'vid_id':vid_id,
            'npas':npa.objects.filter(is_active = 1).filter(vid = vid_id).filter(vid_del = vid_del_id).order_by("date"),
            'npa':npa.objects.filter(is_active = 1).filter(vid = vid_id).filter(vid_del = vid_del_id).first(),
            'year':datetime.now().year,
            
        }
    )

