from cgi import print_exception
from django.shortcuts import redirect, render
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container
from nutrisur.forms import Products_upload_form
from nutrisur.forms import Categories_upload_form
from nutrisur.forms import Presentations_upload_form


def products_list(request):
    search = Healthdrink.objects.all()
    context = {'Healthdrink': search}
    return render(request, "healthdrink.html", context=context)


def categories(request):
    search = Category.objects.all()
    context = {'Category': search}
    return render(request, "category.html", context=context)


def container(request):
    search = Container.objects.all()
    context = {'Container': search}
    return render(request, "container.html", context=context)


def create_products(request):
    print(request.POST)

    if request.method == 'POST':
        form = Products_upload_form(request.POST)

        if form.is_valid():
            Healthdrink.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                country=form.cleaned_data['country']
            )
            return redirect(products_list)

    elif request.method == 'GET':
        form = Products_upload_form
        context = {'form': form}
        return render(request, 'products_load.html', context=context)


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
        return render(request, 'category_load.html', context=context)


def create_presentations(request):
    print(request.POST)

    if request.method == 'POST':
        form = Presentations_upload_form(request.POST)

        if form.is_valid():
            Container.objects.create(
                tipo=form.cleaned_data['tipo'],
                volumen=form.cleaned_data['volumen'],
            )
            return redirect(container)

    elif request.method == 'GET':
        form = Presentations_upload_form
        context = {'form': form}
        return render(request, 'presentation_load.html', context=context)

def redirect_search(request):
    search = request.GET['search']
    search = Healthdrink.objects.filter(name__icontains=search)
    context = {'search': search}
    return render(request, 'search_any_products.html', context=context)
  

