from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from datetime import datetime
from django.contrib import messages
from .models import Todo
from django.views import View
# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'app/index.html', {'todos':todos})

def detail(request, id):
    todo = get_object_or_404(Todo, pk=id)
    return render(request, 'app/detail.html', {'todo':todo})


def delete_todo(request):
    if request.method == 'POST':
        todo = request.POST.get('todos')
        print(todo)
        Todo.objects.filter(id=todo).delete()
        return redirect('/')

class Adding(View):
    def get(self, request):
        return render(request, "App/add_todo.html")

    def post(self,request):

        if request.method == "POST":
            todo_name = request.POST.get('name')
            desc = request.POST.get('desc')
            # completed = request.POST.get('completed')
            # if completed == 'Yes':
            #     completed = True
            # else:
            #     completed = False
            todo = Todo(todo_name=todo_name, desc=desc,  pub_date = datetime.today())
            todo.save()
            messages.success(request, 'Your todo has been published!')
        return redirect('/')
