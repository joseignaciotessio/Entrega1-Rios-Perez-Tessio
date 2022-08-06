from django import forms    

class formulario_productos(forms.form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    pais = forms.CharField()