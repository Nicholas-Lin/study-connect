from django.urls import path
from .views import ProfileDetailView
from .views import profile

urlpatterns = [
    path('', profile, name='profile-edit'),
    path('<str:slug>/', ProfileDetailView.as_view(), name='profile-detail'),
]