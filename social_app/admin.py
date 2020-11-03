from django.contrib import admin

from .models import Course, StudentCourse

# Register your models here.
admin.site.register(Course)
admin.site.register(StudentCourse)