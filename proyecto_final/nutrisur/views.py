from multiprocessing import context
from django.shortcuts import render
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container

def Healthdrink(request):
    micontext = {'Healthdring ': Healthdrink}
    return render (request,"healthdrink.html", context = micontext)

def Category(request):
    micontext = {'Category ': Category}
    return render (request,"category.html", context = micontext)

def Container(request):
    micontext = {'Container ': Container}
    return render (request,"container.html", context = micontext)

