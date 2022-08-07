from cgi import print_exception
from contextlib import redirect_stderr
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
    print(request.POST)
    
    if request.method == 'POST':
        form = Formulario_carga_productos(request.POST)
        
        if form.is_valid():
            Healthdrink.objects.create(
                name = form.cleaned_data ['name'],
                description = form.cleaned_data ['description'],
                price = form.cleaned_data ['price'],
                country = form.cleaned_data ['country']
            )
            
            return redirect(Healthdrink)
        
    elif request.method == 'GET':
        form = Formulario_carga_productos
        context ={'form':form}
        return render(request,'carga_productos.html',context=context)

