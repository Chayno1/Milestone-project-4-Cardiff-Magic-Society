from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.profile_info, name='order_history'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]