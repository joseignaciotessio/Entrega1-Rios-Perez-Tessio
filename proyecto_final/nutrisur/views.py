from django.shortcuts import render
from nutrisur.models import Healthdrink
from nutrisur.models import Category

def products(request):
    micontext = {'Healthdring ': Healthdrink}
    return render (request,"products.html", context = micontext)

def Category(request):
    micontext = {'Category ': Category}
    return render (request,"category.html", context = micontext)

