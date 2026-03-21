from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView


from todo_app.forms import ToDoItemForm
from .models import ToDoItem
from .forms import ToDoItemForm


class ToDoAppIndexView(ListView):
    template_name = "todo_app/index.html"
    queryset = ToDoItem.objects.all().order_by("-id")[:3]
 
 
class ToDoAppView(ListView):
    model = ToDoItem
    
    
class ToDoAppDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all() 
    

class ToDoDetailView(DetailView):
    model = ToDoItem


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemForm
    # fields = ("title", "description") #если нет надобности в кастомной форме
