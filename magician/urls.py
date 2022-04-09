from django.urls import path
from . import views

urlpatterns = [
    path('', views.magician, name='magician'),
    path('edit/', views.edit_advert, name='edit_advert'),
]