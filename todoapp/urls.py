from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('list/', todo_list_view, name='todo_list'),
    path('create/', todo_create_view, name='todo_create'),
    path('delete/<int:todo_id>/', todo_delete_view, name='todo_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update-status/', update_status_view, name='update_status'),
]
