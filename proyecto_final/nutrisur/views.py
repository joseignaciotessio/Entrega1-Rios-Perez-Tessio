from django.shortcuts import render
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container

def productos(request):
    conulta_h = Healthdrink.objects.all()
    micontext = {'Healthdrink': conulta_h}
    return render (request,"healthdrink.html", context = micontext)

def categorias(request):
    conulta_c = Category.objects.all()
    micontext = {'Category': conulta_c}
    return render (request,"category.html", context = micontext)

def envases(request):
    conulta_r = Container.objects.all()
    micontext = {'Container': conulta_r}
    return render (request,"container.html", context = micontext)

def formulario_prod(request):
    return render(request, "formulario.html", context={})