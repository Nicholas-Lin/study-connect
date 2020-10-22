from django.db import models

# Create your models here.
class Course(models.Model):
    subject = models.CharField(max_length=4)
    catalog_number = models.CharField(max_length=4)
    class_title = models.CharField(max_length=100)