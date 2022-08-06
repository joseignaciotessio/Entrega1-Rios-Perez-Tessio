
from django import forms

class FormularioCarga(forms.Form):

    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()


