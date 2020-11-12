from django.urls import path
from .views import profile_list, group_list, home

urlpatterns = [
    path('', home, name='finder-home'),
    path('buddy/', profile_list, name='finder-buddy'),
    path('group/', group_list, name='finder-group'),
]