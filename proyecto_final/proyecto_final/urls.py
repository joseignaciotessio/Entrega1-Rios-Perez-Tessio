from django.contrib import admin
from django.urls import path, include   
from nutrisur.views import create_products, products, categories, containers, create_categories, create_presentations, search_products, index, sale


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', products, name ='Healthdrink'),
    path('', index, name='index'),
    path('Category/',categories, name = 'Category'),
    path('Container/', containers, name = 'Container'),
    path('Products_upload_form/',create_products, name = 'Products_upload_form'),
    path('Categories_upload_form/',create_categories, name = 'Categories_upload_form'),
    path('create_presentaciones/',create_presentations, name = 'create_presentaciones'),
    path('search_products/',search_products, name = 'search_products'),
    path('users/', include('users.urls')),
    path('sale/', sale, name ='sale')
]
