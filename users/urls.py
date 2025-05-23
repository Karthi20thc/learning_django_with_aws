from django.urls import path
from .views.views import CustomUserListView, UserListCreateView

urlpatterns = [
    path('get-users/', CustomUserListView.as_view(), name='user-list-create'),
    path('create-user/', UserListCreateView.as_view(), name='user-list-create'),
]
