from django.urls import path
from . import views

urlpatterns = [
    path('', views.magician, name='magician'),
    path('add/', views.add_hire, name='add_advert'),
    path('edit/<int:advert_id>/', views.edit_advert, name='edit_advert'),
]
