from django.urls import path
from . import views


urlpatterns = [
    path('sign-up/', views.create_user, name='sign-up'),
    path('login-in/', views.login_view, name='login-in'),
    path('logout/', views.logout_view, name='logout'),
    path ('reset/', views.reset_pass, name='forgot-password'),
    path('reset/get-link', views.get_link, name='get-link')
]