from django.db import models
#from django.contrib.auth.mixins import LoginRequiredMixin


class Healthdrink(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500,null=True,blank=True)
    price = models.FloatField()
    country = models.CharField(max_length=40)
    
class Category(models.Model):
    categoria = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=150,null=True,blank=True)
    activo = models.BooleanField(default=True)

class Container(models.Model):
    tipo = models.CharField(max_length=50,null=True,blank=True)
    volumen = models.IntegerField()
    
class Sale(models.Model):
    oferta = models.CharField(max_length=50)
    descuento = models.IntegerField()