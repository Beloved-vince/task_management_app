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
    """
        Allow Authenticated user to add task.\
        if a non authenticated user want to add task,\
            a redirection will occur to prompt the user to login
    """
    user_id = request.user.id
    task = Task.objects.filter(user=request.user.id)

    # if request.user.is_authenticated:
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            try:
                to_base = Task.objects.create(user_id=user_id, title=title, description=description)
                to_base.save()
                # return  redirect('add-task')
            except IntegrityError:
                return HttpResponse(F'USER ID NO {user_id}')
    return render(request, 'notes_dashboard.html', {'tasks': task})



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    from django.http import HttpResponse
    try:
        task = get_object_or_404(Task, id=pk, user=request.user)
        task.delete()
    except Exception as e:
        print(e)
    return HttpResponse(status=204)

@api_view(['GET'])
def home(request):
    """Render home  page function on call"""
    return render(request, 'base.html')