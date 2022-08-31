

from django.shortcuts import redirect, render
from nutrisur.models import Healthdrink
from nutrisur.models import Category
from nutrisur.models import Container

from nutrisur.models import Sale
from nutrisur.models import About
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, CreateView






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

def search_products(request):
    search = request.GET['search']
    consulta = Healthdrink.objects.filter(name__icontains=search) 
    context = {'Healthdrink': consulta}
    return render(request,'search_any_products.html', context=context)


def index(request):
    return render(request, 'index.html')



def about(request):
    consulta = About.objects.all()
    context = {'About': consulta}
    return render(request, "about.html", context=context) 


@login_required
def sale(request):
    consulta = Sale.objects.all()
    context = {'Sale': consulta}
    return render(request, "sale.html", context=context) 

class List_products(ListView):
    model = Healthdrink
    template = 'list_products.html'


	
#nutrisur/healthdrink_list.html

class Create_product(CreateView):  
    model = Healthdrink
    template_name = 'create_article.html'
    fields = '__all__'
    #success_url = '/articles/list-articles/'"""