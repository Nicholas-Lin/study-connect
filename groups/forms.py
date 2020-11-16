from django import forms
from django.contrib.auth.models import User
from .models import Profile
from groups.models import Group
from django.forms.models import inlineformset_factory
from social_app.models import StudentCourse, Course


class MessageGroup(forms.Form):
    #Email = User.email
    Subject = forms.CharField()
    emailContent = forms.CharField(label = "Message", widget = forms.Textarea(attrs = {'rows': 4, 'cols': 40}))
    def __str__(self):
        return self.Email