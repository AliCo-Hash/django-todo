from django.db import models

class ToDoNote(models.Model):
  note = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)
  created_date = models.DateField(auto_now_add=True)