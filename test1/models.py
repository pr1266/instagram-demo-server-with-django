from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
"""
class CustomUser(AbstractUser):

    username   = models.CharField(max_length = 250, primary_key = True)
    password   = models.CharField(max_length = 250)
    role       = models.CharField(max_length = 250, null = True)
    last_visit = models.DateTimeField(null = True, blank = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username"""

class City(models.Model):
    pass 

class Address(models.Model):
    pass

class Customer(models.Model):
    pass

class Platform(models.Model):
    pass


class G_Category(models.Model):
    pass

class Game(models.Model):
    pass

class GameOrder(models.Model):
    pass

class GameDelivery(models.Model):
    pass

class Accessory(models.Model):
    pass

class AccessoryOrder(models.Model):
    pass

class AccessoryDelivery(models.Model):
    pass