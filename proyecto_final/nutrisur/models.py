from django.db import models

class Healthdrink(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    country = models.TextField(max_length=500)
    
class Category(models.Model):
    categoria = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(max_length=150,null=True,blank=True)
    activo = models.BooleanField(default=True)

class Container(models.Model):
    tipo = models.CharField(max_length=50,null=True,blank=True)
    volumen = models.IntegerField(null=True,blank=True)
    
