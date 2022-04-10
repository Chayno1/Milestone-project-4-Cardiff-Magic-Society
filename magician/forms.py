from django import forms
from .models import Performer


class PerformerForm(forms.ModelForm):
    class Meta:
        model = Performer
        exclude = ('user',)