from django.shortcuts import render
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container
from nutrisur.forms import Formulario_carga_productos

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
    print(request.method)
    if request.method =="POST":
        print(request.POST)
    return render(request, "formulario.html", context={})

def create_products(request):
    
    if request.method == 'POST':
        pass
        
        """productos = Healthdrink.objects.all()
        context = {}
    
        if len(productos) >= 2:
            nuevo_producto = Healthdrink.objects.create(name = 'granola',
            description = 'barrita con granola',
            price = 580, 
            country = 'Bolivia')

            context = {
            'nuevo_producto':nuevo_producto
            }
    """
    elif request.method == 'GET':
        form = Formulario_carga_productos
        context ={'form':form}
        return render(request,'nutrisur/carga_productos.html',context=context)