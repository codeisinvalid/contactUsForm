from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, default='admin')
    email = models.EmailField(max_length=100,default='admin@gmail.com')
    subject = models.TextField(max_length=200, default='admin')
    message  = models.TextField(default='admin')

    def __str__(self):
        return self.name
