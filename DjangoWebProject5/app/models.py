"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Years (models.Model):     
     name = models.CharField(max_length = 4) 
     is_active = models.IntegerField(default = 1, 
                                    blank = True, 
                                    null = True, 
                                    help_text ='1->активно, 0->Не активно',  
                                    choices =( (1, 'активно'), (0, 'Не активно') ) )


     class Meta:
            verbose_name = 'Год'
            verbose_name_plural = 'Года'
           
     def __str__(self):
        return self.name 
    
class npa (models.Model):
     year = models.ForeignKey(Years,null=True , on_delete = models.SET_NULL)
     vid_del = models.IntegerField(default = 1,
                                    verbose_name=u"Вид деятельности", 
                                    blank = True, 
                                    null = True, 
                                    help_text ='1->ОД, 0->АХД',  
                                    choices =( (1, 'ОД'), (0, 'АХД') ) )
     vid = models.IntegerField(default = 1, 
                                    verbose_name=u"Вид", 
                                    blank = True, 
                                    null = True, 
                                    help_text ='1->Приказы, 0->Распоряжение',  
                                    choices =( (1, 'Приказы'), (0, 'Распоряжение') ) )
     nomer = models.CharField(max_length = 10,verbose_name=u"Номер") 
     date = models.DateTimeField(verbose_name=u"Дата")
     name = models.CharField(max_length = 1000,verbose_name=u"Наименовение") 
     status = models.IntegerField(default = 1,
                                    verbose_name=u"Статус", 
                                    blank = True, 
                                    null = True, 
                                    help_text ='1->Действующий, 0->Утратил силу',  
                                    choices =( (1, 'Действующий'), (0, 'Утратил силу') ) )
     kol_list = models.IntegerField(default = 1,
                                    verbose_name=u"Количество страниц документа", 
                                    blank = True, 
                                    null = True)
     kol_prl = models.IntegerField(default = 1,
                                    verbose_name=u"Количество страниц приложения", 
                                    blank = True, 
                                    null = True)
     razrab = models.CharField(max_length = 50, verbose_name=u"Разработчик") 
     document = models.FileField(upload_to='./%Y/%m/%d/', verbose_name=u"Документ")    
     is_active = models.IntegerField(default = 1,
                                    verbose_name=u"----------",
                                    blank = True, 
                                    null = True, 
                                    help_text ='1->активно, 0->Не активно',  
                                    choices =( (1, 'активно'), (0, 'Не активно') ) ) 
     
     class Meta:
            verbose_name = 'НПА'
            verbose_name_plural = 'НПА'
           
     def __str__(self):
        return self.name 
    
class link_npa (models.Model):
     name = models.CharField(max_length = 1000,verbose_name=u"Описание") 
     id_npa = models.ForeignKey(npa,null=True , on_delete = models.SET_NULL)                                 
     to_Link_id_npa = models.IntegerField(blank=True, null=True)     
     #test2 = models.ForeignKey(npa,null=True , on_delete = models.SET_NULL)
     
     class Meta:
            verbose_name = 'Cсылки'
            verbose_name_plural = 'Cсылки'
           
     def __str__(self):
        return self.name 