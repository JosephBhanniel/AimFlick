from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Task
from django.urls import reverse
from .forms import RegisterForm, TaskForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, "main/index.html")


@login_required
def user_homepage(request):
    if request.user.is_staff:
        return redirect("/admin")
    else: 
        tasks = Task.objects.filter(user=request.user)
        total_tasks = tasks.count()  # Get the total number of tasks
        completed_tasks = tasks.filter(completed=True).count()  # Get the number of completed tasks
        pending_tasks = total_tasks - completed_tasks  # Calculate the number of pending tasks

        return render(request, "main/user/user_home.html", {
            'tasks': tasks,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
        })

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})



def task_details(request, id):
    task = Task.objects.get(pk=id)
    return HttpResponseRedirect(reverse('task_list'))


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Associate the task with the current user before saving
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("/home")
    else:
        form = TaskForm()
    return render(request, 'main/user/add_task.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'main/user/tasks.html', {'tasks': tasks})


def edit(request, id):
    if request.method == "POST":
        task_instance = Task.objects.get(pk=id)
        form = TaskForm(request.POST, instance=task_instance)
        if form.is_valid():
            form.save()
            return render(request, 'main/user/edit.html', {
                'form': form,
                'success': True
            })
    else:
        task_instance = Task.objects.get(pk=id)
        form = TaskForm(instance=task_instance)
        return render(request, 'main/user/edit.html', {
            'form': form
        })

def delete(request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        task.delete()
        # Add 'success' parameter to the URL
        return HttpResponseRedirect(reverse('task_list') + '?success=True')

def completed(request, id):
    task = Task.objects.get(pk = id)
    task.completed = True
    task.save()

    return HttpResponseRedirect(reverse('task_list'))


