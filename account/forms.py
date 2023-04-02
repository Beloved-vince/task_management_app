from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    """Store form using forms model parent class \
        username: maximum length of 100
        email: email field
        password: Password input"""
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
