from django.shortcuts import render
from account.forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .forms import UserForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view

def create_user(request):
    """This function call allow user to create account and authenticated\
        -- Also verify if there is a valid form input by during registration\
        -- Check if the user gmail exist in google dns server before ssaving to the database\
        -- Redirect to the user page where user can add task and subsequent process.
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                username = cd['username']
                email = cd['email']
                password = cd['password']
                user = User.objects.create(
                    username = username,
                    email=email,
                )
                user.set_password(password)
                user.save()
                return JsonResponse({'message': 'success'})
            except Exception as e:
                messages.error('message', e)
# any additional processing or redirecting
    return render(request, 'index.html')

def login_view(request):
    """Login view check if input data is authenticated,\
        allow login if true else do nothing
    """

    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print (username + password)
            if user is not None:
                login(request, user)
                return render(request, 'notes_dashboard.html')
            messages.error(request, 'username or password is incore')
        except AttributeError as A:
            return HttpResponse(A)

    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('login-in')

@api_view(['GET'])
def reset_pass(request):
    return render(request, 'forgot_password.html')

def get_link(request):
    return render(request, 'confirm.html')