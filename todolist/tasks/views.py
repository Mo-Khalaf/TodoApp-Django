from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render


from .models import Task
from .form import TaskForm
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save() 
            # sdawed
        return redirect('/')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'list.html', context)

def UpdateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)   
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'updatetask.html', context)
    
def DeleteTask(request,pk):
    task=Task.objects.get(id=pk)

    if request.method=='POST':
        task.delete()
        return redirect('/')
    context={'task':task}
    return render(request, 'deletetask.html', context)


# secound commit
# 3
