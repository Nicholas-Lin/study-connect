from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.models import inlineformset_factory
from social_app.models import StudentCourse, Course

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

    def clean_subject(self):
        return self.cleaned_data['subject'].upper()
    
    def clean(self):
        super(StudentCourseForm, self).clean()
        subject = self.cleaned_data.get('subject').upper()
        catalog_number = self.cleaned_data.get('catalog_number')
        if not (subject, catalog_number) in Course.objects.all().values_list('subject', 'catalog_number'):
            self._errors['subject'] = self.error_class([ 
                'Invalid Course'])
        return self.cleaned_data

StudentCourseFormSet = inlineformset_factory(
    Profile, StudentCourse, form=StudentCourseForm, extra=1, can_delete=True
    )
