from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import forms

from django.contrib import messages
from groups.models import Group
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Group
from social_app.models import StudentCourse
from users.models import Profile

from django.http import HttpResponseRedirect

from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from users.models import User
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken



import datetime
from datetime import timedelta

import pytz
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import uuid

service_account_email = "cs3240@cs-3240-291201.iam.gserviceaccount.com"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    filename="credentials.json", scopes=SCOPES
)



def home(request):
    event = create_event()
    context = {
        'event': event.get('htmlLink'),
        'groups': Group.objects.all()
    }
    return render(request, 'groups/home.html', context)

#DataFlair #Send Email
def messageGroup(request, slug):
    model = Profile
    sub = forms.MessageGroup()
    if request.method == 'POST':
        sub = forms.MessageGroup(request.POST)
        subject = str(sub['Subject'].value())
        message = str(sub['emailContent'].value())
        #recepient = User.objects.get(username=slug).first_name
        matches = [val.user.email for val in Group.objects.get(id=slug).members.all()]
        email = EmailMessage(
            subject,
            message,
            #EMAIL_HOST_USER,
            Group.objects.get(id=slug).name + ' has sent a message <studybuddyuva@gmail.com>',
            matches,
            reply_to=[request.user.email],
            headers={'Message-ID': 'foo'},
            )
        email.send()
        return render(request, 'groups/success.html', {'recepient': Group.objects.get(id=slug).name})
    return render(request, 'groups/message_group.html', {'form':sub})

def group_add_self(request, pk, template_name='groups/group_detail.html'):
    memberobj= get_object_or_404(Group, id=pk)

    Group.objects.get(id=pk).members.add(request.user.profile)
    context = {
        'groups': Group.objects.all()
    }

    success_url = reverse_lazy('group-home')
    return HttpResponseRedirect(success_url)

def group_remove_member(request, pk, template_name='groups/group_detail.html'):
    memberobj= get_object_or_404(Group, id=pk)

    Group.objects.get(id=pk).members.remove(request.user.profile)
    context = {
        'groups': Group.objects.all()
    }

    success_url = reverse_lazy('group-home')
    return HttpResponseRedirect(success_url)

class GroupListView(ListView):
    model = Group
    template_name = 'groups/home.html'
    context_object_name = 'groups'

    def get_queryset(self):
        return self.model.objects.filter(members=self.request.user.profile)

class GroupDetailView(DetailView):
    model = Group

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'description', 'course', 'private']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.meeting_url = self.create_event()
        self.object = form.save()
        form.instance.members.add(self.request.user.profile)
        return HttpResponseRedirect(self.get_success_url())

    def save(self):
        instance = forms.ModelForm.save(self)
        instance.members_set.clear()
        instance.members_set.add(self.request.user.profile)
        return instance

    def get_form(self, *args, **kwargs):
        form = super(GroupCreateView, self).get_form(*args, **kwargs)
        form.fields['course'].queryset = StudentCourse.objects.filter(profile = self.request.user.profile)
        return form

    def build_service(self):
        service = build("calendar", "v3", credentials=credentials)
        return service

    def create_event(self):
        service = self.build_service()
        start_datetime = datetime.datetime.now(tz=pytz.utc)
        event = (
            service.events()
            .insert(
                calendarId="studybuddyuva@gmail.com",
                body={
                    "summary": "Foo",
                    "description": "Bar",
                    "start": {"dateTime": start_datetime.isoformat()},
                    "end": {
                        "dateTime": (start_datetime + timedelta(minutes=60)).isoformat()
                    },
                    "conferenceData": {
                        "createRequest": {
                            "requestId": f"{uuid.uuid4().hex}",
                            "conferenceSolutionKey": {"type": "hangoutsMeet"}}},
                },
                conferenceDataVersion=1
            )
            .execute()
        )
        print(event["hangoutLink"])
        return event["hangoutLink"]

class GroupUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Group
    fields = ['name', 'description', 'course', 'meeting_url']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
        
    def test_func(self):
        group = self.get_object()
        if self.request.user == group.owner:
            return True
        return False

class GroupDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('group-home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        group = self.get_object()
        if self.request.user == group.owner:
            return True
        return False
