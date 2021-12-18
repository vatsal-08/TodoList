from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'password1', 'password2']


class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
