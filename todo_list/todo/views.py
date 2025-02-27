from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('add_task')
    else:
        form = UserRegistrationForm()
        return render(request,'todo/register.html',{'form':form})
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'todo/tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')

@login_required
def home(request):
    return render(request, 'todo/home.html')