from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField
    color= models.CharField
    gender= models.CharField


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)