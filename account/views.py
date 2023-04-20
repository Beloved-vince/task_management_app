from django.shortcuts import render
import dns.resolver
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def create_user(request):
    """This function call allow user to create account and authenticated\
        -- Also verify if there is a valid form input by during registration\
        -- Check if the user gmail exist in google dns server before ssaving to the database\
        -- Redirect to the user page where user can add task and subsequent process.
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            domain = email.split('@')[1]
            try:
                mx_records = dns.resolver.query(domain, 'MX')
                mx_record = str(mx_records[0].exchange)[:1]
                if mx_record:
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    messages.success(request, 'Your account has been created')
                    return redirect('login-in')
                else:
                    messages.error(request, 'Your email entered is incorrect')
                    return HttpResponse("email entered is incorrect")
            except Exception as e:
                messages.error(request, f'try again   : {e}')
                return HttpResponse(f'{e}')

    # any additional processing or redirecting you want to do
    return render(request, 'signup.html')

def login_view(request):
    """Login view check if input data is authenticated,\
        allow login if true else do nothing"""
    from django.contrib.auth import authenticate, login
    
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add-task')
            else:
                messages.success(request, 'Your account has been created')
        except AttributeError:
            from django.contrib import messages
            messages.error(request, "Username or password is incorrect")
            # return redirect('sign-up')

    return render(request, 'login.html')