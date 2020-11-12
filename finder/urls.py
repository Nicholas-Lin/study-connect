from django.urls import path
from .views import profile_list

urlpatterns = [
    path('', profile_list, name='finder-home'),
]