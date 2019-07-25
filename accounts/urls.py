from django.urls import path
from . import views

urlpatterns = [
  path('current-user/', views.current_user, name='current_user'),
  path('users', views.UserList.as_view(), name='users')
]
