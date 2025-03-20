from django.urls import path
from .views import signup_view, todo_list_view, todo_create_view, home_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('list/', todo_list_view, name='todo_list'),
    path('create/', todo_create_view, name='todo_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
