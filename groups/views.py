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

def home(request):
    context = {
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

class GroupUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Group
    fields = ['name', 'description', 'course']
    
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
