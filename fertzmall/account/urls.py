from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    


    path('', include('django.contrib.auth.urls')),
	path('', views.dashboard, name='dashboard'),    

    
]  