from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.models import inlineformset_factory
from social_app.models import StudentCourse

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['major', 'year_in_school','bio']
        labels = {
        'major': 'Major',
        'year_in_school': 'Year in School',
        'bio': 'Profile Bio',
        }

class StudentCourseForm(forms.ModelForm):

    class Meta:
        model = StudentCourse
        exclude = ()

StudentCourseFormSet = inlineformset_factory(
    Profile, StudentCourse, form=StudentCourseForm, extra=1, can_delete=True
    )
