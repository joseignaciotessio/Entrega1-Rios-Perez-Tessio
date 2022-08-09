from django.contrib import admin
from .models import Healthdrink
from .models import Container
from .models import Category

# Register your models here.

#admin.site.register(Healthdrink)
@admin.register(Healthdrink)
class Healthdrink_admin(admin.ModelAdmin):
    list_display = ['name','description','price','country']
    

#admin.site.register(Container)
@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ['categoria','description','activo']

@admin.register(Container)
class Category_admin(admin.ModelAdmin):
    list_display = ['tipo','volumen']



#admin.site.register(Category)
#@admin.register(Category)
