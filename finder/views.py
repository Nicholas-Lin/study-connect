from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from social_app.models import StudentCourse
from users.models import Profile
#from django_filters.views import FilterView
from .filters import ProfileFilter


def profile_list(request, template_name='finder/home.html'):
    course = None
    if request.GET.get('course'):
        course_filter = request.GET.get('course')
        course = StudentCourse.objects.get(id=course_filter)
        courses = StudentCourse.objects.filter(subject=course.subject, catalog_number=course.catalog_number).exclude(id=course.id)
        profiles = []
        for c in courses:
            profiles.append(Profile.objects.get(id=c.profile.id))
    else:
        profiles = list(Profile.objects.all())

    context_dict = {'profiles': profiles, 'course': course}
    return render(request, "finder/home.html", context_dict)