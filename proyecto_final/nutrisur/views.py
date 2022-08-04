from django.shortcuts import render
from nutrisur.models import healthdrink


def products(request):
    drink = drink.objects.all()
    micontext = {'healthdrink': healthdrink}
    return render (request,"products.html", context = micontext)
