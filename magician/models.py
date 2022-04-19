from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Performer(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField()
    website = models.CharField(max_length=80, null=True, blank=True)
    website_2 = models.CharField(max_length=80, null=True, blank=True)
    Display = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


 
 
 

