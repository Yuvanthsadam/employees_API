from django.urls import path
from employees.views import UserListView, UserDetailView

urlpatterns=[
    path('list/', UserListView.as_view(), name='user-list'),
    path('list/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]