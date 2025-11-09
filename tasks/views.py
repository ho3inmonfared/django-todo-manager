from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    
    context = {'tasks': tasks, 'form': form}
    return render(request,'index.html',context)