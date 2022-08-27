#from re import search
from django.shortcuts import redirect, render
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container
from nutrisur.forms import Products_upload_form
from nutrisur.forms import Categories_upload_form
from nutrisur.forms import Presentations_upload_form
from nutrisur.models import Sale
from nutrisur.models import About
from django.contrib.auth.decorators import login_required

def products(request):
    consulta = Healthdrink.objects.all()
    context = {'Healthdrink': consulta}
    return render(request, "healthdrink.html", context=context)


def categories(request):
    consulta = Category.objects.all()
    context = {'Category': consulta}
    return render(request, "category.html", context=context)


def containers(request):
    consulta = Container.objects.all()
    context = {'Container': consulta}
    return render(request, "container.html", context=context)

@login_required
def create_products(request):
    print(request.POST)

    if request.method == 'POST':
        form = Products_upload_form(request.POST, request.FILES)

        if form.is_valid():
            Healthdrink.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                country=form.cleaned_data['country'],
                image = form.cleaned_data['image']
            )
            return redirect(products)

    elif request.method == 'GET':
        form = Products_upload_form
        context = {'form': form}
        return render(request, 'products_load.html', context=context)

@login_required
def create_categories(request):
    print(request.POST)

    if request.method == 'POST':
        form = Categories_upload_form(request.POST)

        if form.is_valid():
            Category.objects.create(
                categoria=form.cleaned_data['categoria'],
                description=form.cleaned_data['description'],
            )
            return redirect(categories)

    elif request.method == 'GET':
        form = Categories_upload_form
        context = {'form': form}
        return render(request, 'search_any_products.html', context=context)

@login_required
def create_presentations(request):
    print(request.POST)

    if request.method == 'POST':
        form = Presentations_upload_form(request.POST)

        if form.is_valid():
            Container.objects.create(
                tipo=form.cleaned_data['tipo'],
                volumen=form.cleaned_data['volumen'],
            )
            return redirect(containers)

    elif request.method == 'GET':
        form = Presentations_upload_form
        context = {'form': form}
        return render(request, 'presentations_load.html', context=context)


def search_products(request):
    search = request.GET['search']
    consulta = Healthdrink.objects.filter(name__icontains=search) 
    context = {'Healthdrink': consulta}
    return render(request,'search_any_products.html', context=context)


def index(request):
    return render(request, 'index.html')

@login_required
def sale(request):
    consulta = Sale.objects.all()
    context = {'Sale': consulta}
    return render(request, "sale.html", context=context) 

def about(request):
    consulta = About.objects.all()
    context = {'About': consulta}
    return render(request, "about.html", context=context) 

@login_required
def list_products(request):
    if request.user.is_authenticated:
            products = Healthdrink.objects.all()
            context = {'products':products}
            return render(request, 'products_list.html', context=context)

    return redirect('login')


@login_required
def delete_product(request, pk):
    if request.method == 'GET':
        products = Healthdrink.objects.get(pk=pk)
        context = {'products':products}
        return render(request, 'delete_product.html', context=context)
    elif request.method == 'POST':
        product = Healthdrink.objects.get(pk=pk)
        product.delete()
        return redirect(products)
 
@login_required   
def update_product(request, pk):
    if request.method == 'POST':
        form = Products_upload_form(request.POST)
        if form.is_valid():
            product = Healthdrink.objects.get(id=pk)
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.save()

            return redirect(Healthdrink)


    elif request.method == 'GET':
        product = Healthdrink.objects.get(id=pk)

        form = Products_upload_form(initial={'name':product.name,'price':product.price,'description':product.description,})
        context = {'form':form}
        return render(request, 'update_product.html', context=context)



