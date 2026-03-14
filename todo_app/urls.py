from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.ToDoAppIndexView.as_view(), name='index'),
    path('<int:pk>/', views.ToDoDetailView.as_view(), name='detail'),
    path('list/', views.ToDoAppView.as_view(), name='list'),
    path('done/', views.ToDoAppDoneView.as_view(), name='done'),
]