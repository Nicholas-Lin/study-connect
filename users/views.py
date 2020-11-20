from django.shortcuts import render, redirect , get_object_or_404
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .forms import UserUpdateForm, ProfileUpdateForm, StudentCourseFormSet
from django.contrib import messages
from django.views.generic import DetailView
from .models import Profile
from groups.models import Group

from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from mysite.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

from django.core.mail import EmailMessage
from django.views.generic.edit import FormMixin 


# Create your views here.

#DataFlair #Send Email
def message(request, slug):
    model = Profile
    sub = forms.Message()
    if request.method == 'POST':
        sub = forms.Message(request.POST)
        subject = str(sub['Subject'].value())
        message = str(sub['emailContent'].value())
        recepient = User.objects.get(username=slug).first_name
        email = EmailMessage(
            subject,
            message,
            #EMAIL_HOST_USER,
            request.user.first_name + ' has sent you a message from study connect <studybuddyuva@gmail.com>',
            [User.objects.get(username=slug).email],
            reply_to=[request.user.email],
            headers={'Message-ID': 'foo'},
            )
        email.send()
        return render(request, 'users/success.html', {'recepient': recepient})
    return render(request, 'users/message_form.html', {'form':sub})

def login(request):
    return render(request, 'users/login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile) # add request.FILES as second parameter if using profile image
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('profile-edit') # start GET request
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'user_form': u_form,
        'profile_form' : p_form
    }

    return render(request, 'users/profile.html', context)

def profile_detail(request, slug, template_name='users/profile_detail.html'):
    profile= get_object_or_404(Profile, user__username=slug)

    if request.GET.get('group'):
        group_id = request.GET.get('group')
        Group.objects.get(id=group_id).members.add(profile)
        context_dict = {'object': request.user.profile}
        success_url = reverse_lazy('group-home')
        return HttpResponseRedirect(success_url)

    context_dict = {'object': profile}
    return render(request, "users/profile_detail.html", context_dict)

class ProfileDetailView(DetailView):
    model = Profile

    def get_slug_field(self):
        return 'user__username'
    
class ProfileStudentCourseUpdate(UpdateView):
    model = Profile
    fields = []
    success_url = reverse_lazy('profile-edit-courses')
    
    def get_object(self):
        return self.model.objects.get(pk=self.request.user.profile.pk)
    
    def get_context_data(self, **kwargs):
        data = super(ProfileStudentCourseUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['studentcourses'] = StudentCourseFormSet(self.request.POST, instance=self.object)
        else:
            data['studentcourses'] = StudentCourseFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        studentcourses = context['studentcourses']
        with transaction.atomic():
            self.object = form.save()

            if studentcourses.is_valid():
                studentcourses.instance = self.object
                studentcourses.save()
        return super(ProfileStudentCourseUpdate, self).form_valid(form)