from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages

# Create your views here.
def home(request):
    todo=Todo.objects.all()
    return render(request,"base/home.html",{'todo':todo})

def add(request):
    if request.method=="POST":
        title=request.POST['title']
        if title:
            todo=Todo.objects.create(title=title)
        else:
            messages.info(request,'Add a task')
    return redirect('home')


def delete(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')