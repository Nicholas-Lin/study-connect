from django.urls import path
from .views import GroupListView, GroupDetailView, GroupCreateView, GroupUpdateView, GroupDeleteView, group_remove_member
from . import views

urlpatterns = [
    path('', GroupListView.as_view(), name='group-home'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('create/', GroupCreateView.as_view(), name='group-create'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('<int:pk>/removeMember/', group_remove_member, name='group-removeself'),
]