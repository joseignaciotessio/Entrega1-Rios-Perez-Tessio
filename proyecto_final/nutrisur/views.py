from django.shortcuts import render
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container

def products(request):
    micontext = {'Healthdring ': Healthdrink}
    return render (request,"products.html", context = micontext)

def Category(request):
    micontext = {'Category ': Category}
    return render (request,"category.html", context = micontext)

def Container(request):
    micontext = {'Container ': Container}
    return render (request,"container.html", context = micontext)

