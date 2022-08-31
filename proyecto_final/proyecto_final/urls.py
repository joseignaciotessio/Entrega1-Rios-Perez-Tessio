from django.contrib import admin
from django.urls import path, include
from nutrisur.views import products, categories, containers,  index, sale, about \
    , List_products, Create_product
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', products, name ='Healthdrink'),
    path('', index, name='index'),
    path('Category/',categories, name = 'Category'),
    path('Container/', containers, name = 'Container'),
    path('users/', include('users.urls')),
    path('sale/', sale, name ='sale'),
    path('about/', about, name ='about'),
    path('list_products/', List_products.as_view(), name = 'list_products'),
    path('create_product/', Create_product.as_view(), name = 'create_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


