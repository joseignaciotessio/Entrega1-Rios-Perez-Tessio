from django.shortcuts import render
from nutrisur.models import healthdrink


def products(request):
    micontext = {'healthdring ': healthdrink}
    return render (request,"products.html", context = micontext)


