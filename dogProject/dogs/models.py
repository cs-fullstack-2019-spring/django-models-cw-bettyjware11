from django.db import models

# Create your models here.
from django.db import models

# creating dog class to store information
class Dog(models.Model):
    dog_name = models.CharField(max_length=200)
    dog_breed = models.CharField(max_length=200)
    dog_color= models.CharField(max_length=200)
    dog_gender= models.CharField(max_length=200)

# creating account class to store information
class Account(models.Model):
    account_userName = models.CharField(max_length=200)
    account_realName = models.CharField(max_length=200)
    account_accountNumber = models.IntegerField()
    account_balance = models.IntegerField()