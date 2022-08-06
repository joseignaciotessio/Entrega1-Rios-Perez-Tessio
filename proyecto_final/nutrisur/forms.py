from django import forms

class Formulario_carga_productos(forms.Form):

    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=500)
    price  = forms.IntegerField()
    country = forms.CharField(max_length=40)


