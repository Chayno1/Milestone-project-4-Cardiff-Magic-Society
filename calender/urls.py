from django.urls import path
from . import views

urlpatterns = [
    path('', views.calender, name='calender'),
    path('add/', views.add_event, name='add_event'),
]
