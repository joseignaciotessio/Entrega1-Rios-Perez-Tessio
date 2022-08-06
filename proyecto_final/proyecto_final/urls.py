from django.contrib import admin
from django.urls import path,include   
 
from nutrisur.views import Healthdrink, Category, Container

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', Healthdrink, name ='Healthdrink'),
    path('Category/', Category, name = 'Category'),
    path('Container/', Container, name = 'Container')
]
