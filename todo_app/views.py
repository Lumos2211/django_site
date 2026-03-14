from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ToDoItem


class ToDoAppIndexView(ListView):
    template_name = "todo_app/index.html"
    queryset = ToDoItem.objects.all().order_by("-id")[:3]
 
 
class ToDoAppView(ListView):
    model = ToDoItem
    
    
class ToDoAppDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all() 
    
class ToDoDetailView(DetailView):
    model = ToDoItem