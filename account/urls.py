from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.create_user, name='sign-up'),
    path('login-in', views.login_view, name='login-in')
    # path('home/', create_user)
]