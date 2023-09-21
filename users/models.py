from django.db import models

class User(models.Model):
    firstname = models.CharField(verbose_name="First Name", max_length=100)
    lastname = models.CharField(verbose_name="Last Name", max_length=100)
    age = models.PositiveIntegerField(verbose_name="Age")
    phone_number = models.CharField(verbose_name="Phone Number", max_length=20)
    email = models.EmailField(verbose_name="Email")