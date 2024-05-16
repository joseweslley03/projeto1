from venv import create
from django.db import models

class Todo(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)


class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE,related_name="items")
    text = models.TextField()
    complete = models.BooleanField(default=False)


