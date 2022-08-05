from django.contrib import admin
from django.urls import path
from nutrisur.models import Healthdrink
from nutrisur.models import Category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nutrisur', Healthdrink),
    path('category', Category)
]
