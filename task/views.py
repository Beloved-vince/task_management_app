from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import TaskForm

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def add_task(request):
    """Allow Authenticated user to add task.\
        if a non authenticated user want to add task,\
            a redirection will occur to prompt the user to login"""
    user_id = request.user.id
    task = Task.objects.filter(user=request.user.id)
    
    # if request.user.is_authenticated:
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            due_date = form.cleaned_data['due_date']
            try:
                to_base = Task.objects.create(user=user_id, name=name, description=description, due_date=due_date)
                to_base.save()
                return  redirect('add-task')
            except IntegrityError:
                return HttpResponse(F'USER ID NO {user_id}')    
    return render(request, 'user.html', {'tasks': task})


@api_view(['GET'])
def home(request):
    """Render home  page function on call"""
    return render(request, 'base.html')