from django.contrib import admin
from django.urls import path, include   
from nutrisur.views import create_products, products, categories, containers, create_categories, create_presentations, search_products, index, sale, about
from django.conf.urls.static import static
from django.conf import settings
from nutrisur.views import delete_product, update_product,list_products
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
    path('sale/', sale, name ='sale'),
    path('about/', about, name ='about'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
    path('list_products/', list_products, name='list_products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
