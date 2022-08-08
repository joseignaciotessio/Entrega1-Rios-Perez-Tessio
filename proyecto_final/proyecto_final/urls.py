from django.contrib import admin
from django.urls import path   
from nutrisur.views import create_products, productos, categorias, envases, create_categorias, create_presentaciones, redirect_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', productos, name ='Healthdrink'),
    path('Category/', categorias, name = 'Category'),
    path('Container/', envases, name = 'Container'),
    path('Formulario_carga_productos/',create_products, name = 'Formulario_carga_productos'),
    path('Formulario_carga_categorias/',create_categorias, name = 'Formulario_carga_categorias'),
    path('create_presentaciones/',create_presentaciones, name = 'create_presentaciones'),
    path('redirect_search/',redirect_search, name = 'redirect_search')
]
