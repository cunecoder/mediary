from django import forms
from .models import Event, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
                'id': 'location-input'
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

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': "Enter your email...",
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']  # 'username' is actually 'email' due to USERNAME_FIELD

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})