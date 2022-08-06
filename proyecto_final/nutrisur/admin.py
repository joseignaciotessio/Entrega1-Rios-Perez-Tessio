from django.contrib import admin
from .models import Healthdrink
from .models import Container
from .models import Category

# Register your models here.
admin.site.register(Healthdrink)
admin.site.register(Container)
admin.site.register(Category)