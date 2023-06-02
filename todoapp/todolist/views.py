from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ToDo

def index(requests):
    todos = ToDo.objects.all()
    return render(requests, 'todoapp/index.html', {'todo_list': todos, 'title': 'Home'}) 


@require_http_methods(['POST'])
def add(requests):
    title = requests.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('index')
   
   
def update(requests, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete 
    todo.save()
    return redirect('index')

    
def delete(requests, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

    