from django.db import models

# Create your models here.
class Course(models.Model):
    subject = models.CharField(max_length=4)
    catalog_number = models.CharField(max_length=4)
    class_section = models.CharField(max_length=4)
    class_number = models.IntegerField()
    class_title = models.CharField(max_length=100)
    class_topic_formal_desc = models.CharField(max_length=500)
    instructor = models.CharField(max_length=50)
    enrollment_capacity = models.PositiveSmallIntegerField()
    meeting_days = models.CharField(max_length=7)
    meeting_time_start = models.CharField(max_length=10)
    meeting_time_end = models.CharField(max_length=10)
    term = models.CharField(max_length=10)
    term_desc = models.CharField(max_length=15)