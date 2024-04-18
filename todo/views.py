from django.shortcuts import render
from .models import ToDoNote

def todo_list(request):
  todo_notes = ToDoNote.objects.all()
  return render(request, 'todo/todo_list.html', {'todo_notes': todo_notes})