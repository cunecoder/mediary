from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Event, User

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
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': "Enter your username...",
                'class': 'form-control',
                'required': 'required',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': "Enter your email...",
                'class': 'form-control',
                'required': 'required',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username is required.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        if User.objects.filter(email__iexact=email.lower()).exists():
            raise forms.ValidationError("This email is already registered.")
        return email.lower()

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email...',
        'required': 'required'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password...'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure the username field (which is email) is properly labeled
        self.fields['username'].label = 'Email'

    def clean_username(self):
        email = self.cleaned_data.get('username')
        if email:
            return email.lower()  # Normalize email to lowercase
        raise forms.ValidationError("Email is required.")