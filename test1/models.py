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
    name = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.name 

class Address(models.Model):
    address     = models.CharField(max_length = 300, null = True)
    postal_code = models.CharField(max_length = 10, null = True) 
    city        = models.ForeignKey(City, on_delete = models.CASCADE)

    def __str__(self):

        return self.city.name + ' ' + self.address

class Platform(models.Model):
    name = models.CharField(max_length = 30, null = True)

    def __str__(self):
        return self.name

class G_Category(models.Model):
    c_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.c_name

class Game(models.Model):
    name    = models.CharField(max_length = 100)
    describ = models.TextField()
    gameCat = models.ForeignKey(G_Category, on_delete = models.CASCADE)
    gamePlt = models.ForeignKey(Platform, on_delete = models.CASCADE)
    price   = models.IntegerField(default = 0)
    picture = models.ImageField(upload_to = 'pic_folder/')

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