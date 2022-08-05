from django.contrib import admin
from django.urls import path    
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Healthdrink/', Healthdrink, name ='Healthdrink'),
    path('Category/', Category, name = 'Category'),
    path('Container/', Container, name = 'Container')
]
