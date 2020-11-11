from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Group
from social_app.models import StudentCourse


def home(request):
    context = {
        'groups': Group.objects.all()
    }
    return render(request, 'groups/home.html', context)

class GroupListView(ListView):
    model = Group
    template_name = 'groups/home.html'
    context_object_name = 'groups'

class GroupDetailView(DetailView):
    model = Group

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'description', 'course', 'private']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

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
