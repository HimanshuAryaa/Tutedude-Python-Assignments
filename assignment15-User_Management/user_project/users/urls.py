from django.urls import path
from.views import UserList, UserDetail

urlpatterns = [
    path('profiles/', UserList.as_view(), name='user-list'),
    path('profiles/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]