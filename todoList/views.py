import os
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# @login_required
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to a success page.
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('login')
            #return redirect('some-success-url')  # Redirect to a success page
    else:
        form = UserCreationForm()  # Display an empty form for GET request
    return render(request, 'registration/register.html', {'form': form})

@login_required
def task_list(request):

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todoList/list.html', {'tasks': tasks})


@login_required
def task_detail(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    return render(request, 'todoList/detail.html', {'task': task})

#@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('list')
    else:
        form = TaskForm()
    return render(request, 'todoList/form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoList/form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect('list')

