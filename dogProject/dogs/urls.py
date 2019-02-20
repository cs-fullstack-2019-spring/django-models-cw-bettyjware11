from django.urls import path

from . import views

urlpatterns = [
    path('dog1', views.dogs, name='dog1'),
    path('dog2', views.dogs, name='dog2'),
    path('dog3', views.dogs, name='dog3'),
]