import requests
import json
from scoail_app.models import Course

url = 'https://api.devhub.virginia.edu/v1/courses'
data = requests.get(url).json()

unique_courses = list()
for i in data["class_schedules"]["records"]:
    unique_courses.append((i[0], i[1], i[4]))

unique_courses = set(unique_courses)
for i in unique_courses:
    q = Course(subject = i[0], catalog_number = i[1], class_title = i[2])
    q.save()