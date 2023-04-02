from django import forms
from  .models import Task
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    """Store form using forms model parent class \
        username: maximum length of 100
        email: email field
        password: Password input"""
    class Meta:
        """return username email and password to view"""
        model = Task
        fields = ['name', 'description', 'due_date']