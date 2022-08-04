from django.db import models

class healthdrink(models.Model):
    nombre = models.CharField(max_length=50, null=True,blank=True)
    descripcion = models.TextField(max_length=500,null=True,blank=True)
    precio = models.FloatField(null=True,blank=True)
    country = models.Text(max_length=500,null=True,blank=True)