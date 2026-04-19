from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# defining an application namespace with the app_name variable. This allows you to organize URLs by application and use the name when referring to them.
app_name = 'fertzmall_scrapers'

urlpatterns = [
path('', views.product_list, name='product_list'), #doesn’t take any arguments and is mapped to the product_list view.
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('register/', views.register, name='register'),
path('dashboard/', views.dashboard, name='dashboard'),
path('logged_out/', views.logged_out, name='logged_out'),
]
