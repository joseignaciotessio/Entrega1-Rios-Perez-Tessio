from django import forms

class Formulario_carga_productos(forms.Form):

    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=500)
    price  = forms.IntegerField()
    country = forms.CharField(max_length=40)

class Formulario_carga_categorias(forms.Form):

    categoria = forms.CharField(max_length=50)
    description = forms.CharField(max_length=150)

class Formulario_carga_presentaciones(forms.Form):
    
    tipo = forms.CharField(max_length=50)
    volumen = forms.IntegerField()
