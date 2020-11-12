from django.db import models
from users.models import Profile

# Create your models here.
class Course(models.Model):
    subject = models.CharField(max_length=4)
    catalog_number = models.CharField(max_length=4)
    class_title = models.CharField(max_length=100)

class StudentCourse(models.Model):
    # course = models.OneToOneField(Course, on_delete = models.CASCADE)
    subject = models.CharField(max_length=4, blank=True)
    catalog_number = models.CharField(max_length=4, blank=True)
    difficulty = models.SmallIntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    def __str__(self):
        return self.subject + " " + self.catalog_number