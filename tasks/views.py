from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task added successfully!✔")
            return redirect('index')
        else:
            messages.error(request, "There was an error adding the task. Please try again.❌")
    else:
        form = TaskForm()
        
    
    context = {'tasks': tasks, 'form': form}
    return render(request,'index.html',context)


@login_required
@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, "Task deleted successfully!✔")
    return redirect('index')

@login_required
@require_POST
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    messages.success(request, "Task status updated successfully!✔")
    return redirect('index')

@login_required
def detail_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    context = {'task': task}
    return render(request, 'detail.html', context)