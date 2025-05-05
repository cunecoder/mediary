# mediary/forms.py
# Author: David Marin & Silas Curtis
# Last Updated: 4/27/2025
# Description: This file contains the forms we use for the Mediary website's database.
# * Includes: form for creating an event

from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'description', 'time']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "Event Title...",
                'class': 'form-control my-custom-class',
                'id': 'event-title-input'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': "Enter an address...",
                'class': 'form-control',
                'id': 'location-input'  # Add a unique ID for JavaScript
            }),
            'description': forms.Textarea(attrs={
                'placeholder': "Tell us about it!",
                'rows': 3,
                'cols': 30,
                'class': 'form-control',
            }),
            'time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            })
        }