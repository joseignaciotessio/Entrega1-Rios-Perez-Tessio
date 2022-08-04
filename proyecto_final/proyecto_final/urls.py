from django.contrib import admin
from django.urls import path

from proyecto_final.nutrisur.models import healthdrink

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nutrisur', healthdrink)
]
