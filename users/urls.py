from django.urls import path
from .views import ProfileDetailView, ProfileStudentCourseUpdate
from .views import profile
from .views import message


urlpatterns = [
   
    path('message/<str:slug>/', message, name = 'message'),
    path('', profile, name='profile-edit'),
    path('add/', ProfileStudentCourseUpdate.as_view(), name='profile-edit-courses'),
    path('<str:slug>/', ProfileDetailView.as_view(), name='profile-detail'),
    
]