from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from social_app.models import StudentCourse
from users.models import Profile
from groups.models import Group
#from django_filters.views import FilterView
#from .filters import ProfileFilter

def home(request):
    return render(request, "finder/home.html")

def profile_list(request, template_name='finder/buddy.html'):
    course = None
    if request.GET.get('course'):
        course_filter = request.GET.get('course')
        course = StudentCourse.objects.get(id=course_filter)
        courses = StudentCourse.objects.filter(subject=course.subject, catalog_number=course.catalog_number).exclude(id=course.id)
        profiles = []
        for c in courses:
            profiles.append(Profile.objects.get(id=c.profile.id))
    else:
        profiles = Profile.objects.all()

    context_dict = {'profiles': profiles, 'course': course}
    return render(request, "finder/buddy.html", context_dict)

def group_list(request, template_name='finder/group.html'):
    course = None
    if request.GET.get('course'):
        course_filter = request.GET.get('course')
        course = StudentCourse.objects.get(id=course_filter)
        groups = Group.objects.filter(course__subject=course.subject, course__catalog_number=course.catalog_number).exclude(private=True)
    else:
        groups = Group.objects.all().exclude(private=True)

    context_dict = {'groups': groups, 'course': course}
    return render(request, "finder/group.html", context_dict)