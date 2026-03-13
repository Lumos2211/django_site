from django.contrib import admin

from todo_app.models import ToDoItem

@admin.register(ToDoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = "title", "done"