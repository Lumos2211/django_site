from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.ToDoAppIndexView.as_view(), name='index'),
    path('<int:pk>/', views.ToDoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.ToDoItemUpdateView.as_view(), name='update'),
    path('<int:pk>/confirm-delete/', views.ToDoItemDeleteView.as_view(), name='delete'),
    path('list/', views.ToDoAppView.as_view(), name='list'),
    path('done/', views.ToDoAppDoneView.as_view(), name='done'),
    path('create/', views.ToDoItemCreateView.as_view(), name='create'),
]