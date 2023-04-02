from . import views
from django.urls import path


urlpatterns = [
    path('add-task/', views.add_task, name='add-task'),
    path('home/', views.home),
]