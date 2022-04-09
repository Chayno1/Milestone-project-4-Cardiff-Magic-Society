from django.db import models
from datetime import date
import datetime

# Create your models here.

class Member_status(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    location = models.TextField()
    open_to = models.ForeignKey('Member_status', null=True, blank=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.name