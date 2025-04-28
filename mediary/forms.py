# mediary/forms.py
# Author: David Marin & Silas Curtis
# Last Updated: 4/27/2025
# Description: This file contains the forms we use for the Mediary website's database.
# * Includes: form for creating an event

from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    Form for creating an event

    Attributes:
        Meta: Metadata for the form
    """
    class Meta:
        model = Event
        fields = ['title', 'location', 'description', 'time']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Event Title..."}),
            'location': forms.TextInput(attrs={'placeholder': "Location..."}),
            'description': forms.Textarea(attrs={'placeholder': "Tell us about it!", 'rows': 3, 'cols': 30}),
            'time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }