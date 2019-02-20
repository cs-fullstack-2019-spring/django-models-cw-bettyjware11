from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def dogs(request):
    return HttpResponse("Name, Breed, Color, Gender")

# def dogs(dog2):
#     return HttpResponse("Cali, Shepard, White, Female")
#
# def dogs(dog3):
#     return HttpResponse("Maximus, Collie, Black, Male")