from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_images, name='gallery'),
    path('add/', views.add_image, name='add_image'),
    path('delete/', views.delete_image, name='delete_image'),
]
