from django.shortcuts import render
import dns.resolver
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def create_user(request):
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
            except ObjectDoesNotExist:
                messages.error(request, 'Please sign in with Google')
                return redirect('base.html')
            except Exception as e:
                messages.error(request, f'try again   : {e}')
                return HttpResponse(f'sign-up {e}')

            # any additional processing or redirecting you want to do
        return render(request, 'user.html')

    return render(request, 'signup.html')
