from django.db import models

# Create your models here.

class contactform(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    message=models.TextField(max_length=100)
