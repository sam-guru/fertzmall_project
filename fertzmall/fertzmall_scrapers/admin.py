from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    #creating a display list and registering all the fileds to be displayed
    list_display = ['name', 'image_url', 'price', 'url']

    #creating a filter list (the right filter sidebar) that allows you to filter results by the fields registered
    list_filter = ['name', 'price']

    #creating a search field and defining a list of searchable fields registered
    search_fields = ['name']


    #making posts to be ordered by "price columns by default.
    ordering = ['price']