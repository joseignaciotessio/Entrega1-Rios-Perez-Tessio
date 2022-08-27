from django import forms


class Products_upload_form(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=500)
    price = forms.IntegerField()
    country = forms.CharField(max_length=40)
    image = forms.ImageField(required=False)


class Categories_upload_form(forms.Form):
    categoria = forms.CharField(max_length=50)
    description = forms.CharField(max_length=150)



class Presentations_upload_form(forms.Form):
    tipo = forms.CharField(max_length=50)
    volumen = forms.IntegerField()
 

