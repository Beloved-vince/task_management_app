from django.urls import path
from .views import create_user

urlpatterns = [
    path('sign-up/', create_user, name='sign-up')
    # path('home/', create_user)
]