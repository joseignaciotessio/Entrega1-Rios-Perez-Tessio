from django.contrib import admin
from django.urls import path   
from nutrisur.views import create_products, productos, categorias, envases, create_categorias, create_presentaciones, search_productos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', productos, name ='Healthdrink'),
    path('Category/', categorias, name = 'Category'),
    path('Container/', envases, name = 'Container'),
    path('Formulario_carga_productos/',create_products, name = 'Formulario_carga_productos'),
    path('Formulario_carga_categorias/',create_categorias, name = 'Formulario_carga_categorias'),
    path('Formulario_carga_presentaciones/',create_presentaciones, name = 'Formulario_carga_presentaciones'),
    path("search_products/", search_productos, name = "search_products")
]
