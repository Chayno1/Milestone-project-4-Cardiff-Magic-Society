from django import forms
from .models import Performer


class PerformerForm(forms.ModelForm):
    class Meta:
        model = Performer
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, 
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone Number',
            'description': 'describe service you offer',
            'website': 'website link',
            'website_2': 'social media link',
        }