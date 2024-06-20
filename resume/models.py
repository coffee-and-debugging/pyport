from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
