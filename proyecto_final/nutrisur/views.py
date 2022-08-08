from re import search
from django.shortcuts import redirect, render
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container
from nutrisur.forms import Formulario_carga_productos
from nutrisur.forms import Formulario_carga_categorias
from nutrisur.forms import Formulario_carga_presentaciones


def productos(request):
    consulta = Healthdrink.objects.all()
    context = {'Healthdrink': consulta}
    return render(request, "healthdrink.html", context=context)


def categorias(request):
    consulta = Category.objects.all()
    context = {'Category': consulta}
    return render(request, "category.html", context=context)


def envases(request):
    consulta = Container.objects.all()
    context = {'Container': consulta}
    return render(request, "container.html", context=context)


def create_products(request):
    print(request.POST)

    if request.method == 'POST':
        form = Formulario_carga_productos(request.POST)

        if form.is_valid():
            Healthdrink.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                country=form.cleaned_data['country']
            )
            return redirect(productos)

    elif request.method == 'GET':
        form = Formulario_carga_productos
        context = {'form': form}
        return render(request, 'carga_productos.html', context=context)


def create_categorias(request):
    print(request.POST)

    if request.method == 'POST':
        form = Formulario_carga_categorias(request.POST)

        if form.is_valid():
            Category.objects.create(
                categoria=form.cleaned_data['categoria'],
                description=form.cleaned_data['description'],
            )
            return redirect(categorias)

    elif request.method == 'GET':
        form = Formulario_carga_categorias
        context = {'form': form}
        return render(request, 'carga_categorias.html', context=context)


def create_presentaciones(request):
    print(request.POST)

    if request.method == 'POST':
        form = Formulario_carga_presentaciones(request.POST)

        if form.is_valid():
            Container.objects.create(
                tipo=form.cleaned_data['tipo'],
                volumen=form.cleaned_data['volumen'],
            )
            return redirect(envases)

    elif request.method == 'GET':
        form = Formulario_carga_presentaciones
        context = {'form': form}
        return render(request, 'carga_presentaciones.html', context=context)

def redirect_search(request):
    search = request.GET['search']
    consulta = Healthdrink.objects.filter(name__icontains=search)
    context = {'Healthdrink': consulta}
    return render(request, "search_any_products.html", context=context)
  

