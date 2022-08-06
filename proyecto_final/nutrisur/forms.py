
from django import forms

class FormularioCarga(forms.forms):

    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()


