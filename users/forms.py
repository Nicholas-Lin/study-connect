from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['major', 'year_in_school']