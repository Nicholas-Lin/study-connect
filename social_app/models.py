from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Profile

# Create your models here.
class Course(models.Model):
    subject = models.CharField(max_length=4)
    catalog_number = models.CharField(max_length=4)
    class_title = models.CharField(max_length=100)

class StudentCourse(models.Model):
    # course = models.OneToOneField(Course, on_delete = models.CASCADE)
    subject = models.CharField(max_length=4, blank=True, verbose_name="Subject (ex. CS)")
    catalog_number = models.CharField(max_length=4, blank=True, verbose_name="Catalog Number (ex. 2150)")
    difficulty = models.SmallIntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)], verbose_name="Difficulty from 1 (easy) to 10 (hard)")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    def __str__(self):
        return self.subject + " " + self.catalog_number