from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ToDoItem
from .forms import (ToDoItemCreateForm, ToDoItemUpdateForm)


class ToDoAppIndexView(ListView):
    template_name = "todo_app/index.html"
    # TODO custom qs, arch
    queryset = ToDoItem.objects.all().order_by("-id")[:3]
 
 
class ToDoAppView(ListView):
    queryset = ToDoItem.objects.filter(archived=False)
    
    
class ToDoAppDoneView(ListView):
    # TODO arch
    queryset = ToDoItem.objects.filter(done=True).all() 
    

class ToDoDetailView(DetailView):
    # TODO arch 
    queryset = ToDoItem.objects.filter(archived=False)


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm
    # fields = ("title", "description") #если нет надобности в кастомной форме
    

class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = "_update_form"
    form_class = ToDoItemUpdateForm
    

class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy("todo_app:list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
        
    
