from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'date_of_birth', 'email')
        labels = {
            'name': 'Student Name',
            'date_of_birth': 'Date of Birth',
            'email': 'Email Address',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'sc-input'}),
            'name': forms.TextInput(attrs={'class': 'sc-input', 'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'class': 'sc-input', 'placeholder': 'email@example.com'}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name')
