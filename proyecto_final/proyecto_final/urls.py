from django.contrib import admin
from django.urls import path,include   
from nutrisur.views import productos, categorias, envases, formulario_prod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', productos, name ='Healthdrink'),
    path('Category/', categorias, name = 'Category'),
    path('Container/', envases, name = 'Container'),
    path("formulario/", formulario_prod, name = "formulario")
]
