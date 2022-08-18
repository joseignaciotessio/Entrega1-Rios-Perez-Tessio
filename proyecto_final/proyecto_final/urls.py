from django.contrib import admin
from django.urls import path   
from nutrisur.views import create_products, products_list, categories, container, create_categories, create_presentations, redirect_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', products_list, name ='Healthdrink'),
    path('Category/',categories, name = 'Category'),
    path('Container/', container, name = 'Container'),
    path('Products_upload_form/',create_products, name = 'Products_upload_form'),
    path('Categories_upload_form/',create_categories, name = 'Categories_upload_form'),
    path('create_presentaciones/',create_presentations, name = 'create_presentaciones'),
    path('redirect_search/',redirect_search, name = 'redirect_search')
]
