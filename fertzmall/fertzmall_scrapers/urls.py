from django.urls import path
from . import views

# defining an application namespace with the app_name variable. This allows you to organize URLs by application and use the name when referring to them.
app_name = 'fertzmall_scrapers'

urlpatterns = [
# product views
path('', views.product_list, name='product_list'), #doesn’t take any arguments and is mapped to the product_list view.
]