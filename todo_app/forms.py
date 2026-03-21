from dataclasses import field
from turtle import width
from django import forms

from todo_app.models import ToDoItem

class ToDoItemForm(forms.ModelForm):
    
    class Meta:
        model = ToDoItem
        fields = ("title", "description")
        
        widgets = {
            "description": forms.Textarea(
                attrs={"cols": 20, "rows": 4}
            ),
        }

    