from django.contrib import admin
from django.urls import path
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nutrisur', Healthdrink, name ='Healthdrink'),
    path('nutrisur', Category, name = 'Category'),
    path('nutrisur', Container, name = 'Container')
]
