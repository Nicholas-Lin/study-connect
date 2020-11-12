from django.urls import path
from . import views

urlpatterns = [
    path('', GroupListView.as_view(), name='finder-home'),
]