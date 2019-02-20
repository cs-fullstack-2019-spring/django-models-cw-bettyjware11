from django.db import models

# Create your models here.
from django.db import models


class dogs(models.Model):
    account_userName = models.CharField(max_length=200)
    account_realName = models.CharField(max_length=200)
    account_accountNumber = models.IntegerField(max_length=200)
    account_balance = models.IntegerField(max_length=200)


