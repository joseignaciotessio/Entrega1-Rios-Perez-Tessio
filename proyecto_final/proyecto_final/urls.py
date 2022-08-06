from django.contrib import admin
from django.urls import path,include   
from nutrisur.views import create_products, productos, categorias, envases, formulario_prod
from nutrisur.forms import FormularioCarga


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', productos, name ='Healthdrink'),
    path('Category/', categorias, name = 'Category'),
    path('Container/', envases, name = 'Container'),
    path("formulario/", formulario_prod, name = "formulario"),
    path('FormularioCarga/',create_products, name = 'FormularioCarga')
]
