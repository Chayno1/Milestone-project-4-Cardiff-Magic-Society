from django import forms
from .models import Event, Member_status


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'