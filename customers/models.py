from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField( max_length=255,)
    email = models.EmailField()
    started = models.DateField()
    password = models.CharField( max_length=255,)
