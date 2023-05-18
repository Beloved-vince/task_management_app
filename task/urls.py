from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-task/', views.add_task, name='add-task'),
    path('', views.home),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)