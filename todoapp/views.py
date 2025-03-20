from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .models import Todo
from .forms import TodoForm


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')  # Redirect to the to_do list after signup
    else:
        form = UserCreationForm()
    return render(request, 'todoapp/signup.html', {'form': form})


@login_required
def todo_list_view(request):
    """Display the list of todos for the logged-in user."""
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todoapp/todo_list.html', {'todos': todos})


@login_required
def todo_create_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Assign the logged-in user to the todo item
            todo.save()
            return redirect('todo_list')  # Redirect to the todo list page
    else:
        form = TodoForm()
    return render(request, 'todoapp/todo_create.html', {'form': form})


def home_view(request):
    return render(request, 'todoapp/home.html')
