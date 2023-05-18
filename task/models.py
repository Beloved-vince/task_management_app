from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    """Task parameters
    Args:
        user: user creating task id
        name: task name maximum length 50
        descripption: task description
        status: task status return true if task is completed
        created_at: date of task  created auto now
        updated_at: date of task  updated auto now
        due_date: date task should completed (set by the user )
        completed_date: date task is completed by the assignee(to be added later)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    completed_date = models.DateTimeField(auto_now_add=True)


    