from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.http import HttpResponse
from account.views import create_user


# Create your views here.
# @api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def add_task(request):
    try:
        # user = authenticate(username)
        if request.method == 'POST':
            if request.user.is_authenticated:
                name = request.POST.get('name')
                description = request.POST.get('description')
                due_date = request.POST.get('due_date')
                task = Task.objects.create(name=name, description=description, due_date=due_date)
                if task.clean_fields():
                    task.save()
                    # serializer = TaskSerializer(task, many=True)
                    return render(request, 'user.html')
            else:
                return redirect('sign-up')
    except Exception as e:
        return HttpResponse(f'Error as {e}')
    return render(request, 'user.html')


@api_view(['GET'])
def home(request):
    return render(request, 'base.html')