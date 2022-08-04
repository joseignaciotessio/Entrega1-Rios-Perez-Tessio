from django.db import models

class healthdrink(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    country = models.Text(max_length=500)