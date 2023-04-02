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
                mx_record = str(mx_records[0].exchange)
                if 'google' in mx_record:
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    messages.success(request, 'Your account has been created')
                else:
                    messages.success(request, 'Your account has been created')
                    return HttpResponse("Not possible")
                return redirect('base.html')
            except Exception as e:
                messages.error(request, f'try again   : {e}')
                return HttpResponse(f'{e}')

            # any additional processing or redirecting you want to do
        return render(request, 'user.html')

    return render(request, 'signup.html')

def login_view(request):
    from django.contrib.auth.models import User
    from django.contrib.auth import authenticate
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            user.is_authenticated
            return render(request, 'user.html')
        except AttributeError:
            from django.contrib import messages
            messages.error(request, "Username or password is incorrect")
            # return redirect('sign-up')

    return render(request, 'login.html')