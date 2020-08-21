"""
Definition of urls for DjangoWebProject4.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^$', views.home, name='home'),
    path('', views.home, name='home'),    
    path('document/<int:question_id>/', views.document, name='document'),
    path('org/<int:year_id>/<int:vid_id>/<int:vid_del_id>', views.org, name='org'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


