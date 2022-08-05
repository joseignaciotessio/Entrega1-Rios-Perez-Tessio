from django.db import models

class Healthdrink(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    country = models.TextField(max_length=500)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    stock = models.IntegerField()
    
class Category(models.Model):
    name = models.CharField(max_length=50)    
