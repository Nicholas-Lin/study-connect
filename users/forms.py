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
        fields = ['major', 'year_in_school','course_1','course_2','course_3','course_4']
        labels = {
        'major': 'Major',
        'year_in_school': 'Year in School',
        'course_1': 'course 1 (formatted as: CS2150)',
        'course_2': 'course 2 (formatted as: CS2150)',
        'course_3': 'course 3 (formatted as: CS2150)',
        'course_4': 'course 4 (formatted as: CS2150)',
        }
