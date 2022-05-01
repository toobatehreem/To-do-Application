from datetime import datetime
from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_name = models.CharField(max_length=200)
    desc = models.TextField()
    completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.todo_name