from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
=======
from django.views.generic import ListView
>>>>>>> 04f7a03bae29b79cf4e1a17a3ab241a394bc02cb

from .models import Todo

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World</h1>")

class TodoList(ListView):
    model = Todo
<<<<<<< HEAD
    context_object_name = "tasks"
    
class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")
    
class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")
=======
    context_object_name = "tasks"
>>>>>>> 04f7a03bae29b79cf4e1a17a3ab241a394bc02cb
