from django.urls import path
from .views import ProfileDetailView, ProfileStudentCourseUpdate
from .views import profile

urlpatterns = [
    path('', profile, name='profile-edit'),
    path('add/', ProfileStudentCourseUpdate.as_view(), name='profile-edit-courses'),
    path('<str:slug>/', ProfileDetailView.as_view(), name='profile-detail'),
]