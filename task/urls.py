from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-task/', views.add_task, name='add-task'),
    path('', views.home),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)