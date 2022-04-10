from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('join/', views.join, name='join'),
]
