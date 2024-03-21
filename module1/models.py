from django.db import models
from django.forms import forms


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)

    class Meta:
        db_table = "Register"


class contactus(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    comment = models.TextField(max_length=100)

    class Meta:
        db_table = "contactus"
