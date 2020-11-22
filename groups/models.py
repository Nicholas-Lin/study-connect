from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
from social_app.models import StudentCourse
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(StudentCourse, default='', on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(Profile)
    private = models.BooleanField(default=False)
    meeting_url = models.URLField(default='https://meet.google.com/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})
