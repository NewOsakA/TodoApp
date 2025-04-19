from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

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
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    status_labels = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    return render(request, 'todoapp/todo_list.html', {
        'todos': todos,
        'status_labels': status_labels,
    })


@login_required
def todo_create_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Assign the logged-in user to the to.do item
            todo.save()
            return redirect('todo_list')  # Redirect to the to.do list page
    else:
        form = TodoForm()
    return render(request, 'todoapp/todo_create.html', {'form': form})


@login_required
def todo_delete_view(request, todo_id):
    """Delete a specific todo."""
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo_list')


@csrf_exempt
@login_required
def update_status_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id')
        new_status = data.get('new_status')

        try:
            todo = Todo.objects.get(id=task_id, user=request.user)
            todo.status = new_status
            todo.save()
            return JsonResponse({'success': True})
        except Todo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Todo not found'}, status=404)


def home_view(request):
    return render(request, 'todoapp/home.html')
