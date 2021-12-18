from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.views.generic import FormView
from django.contrib import auth
from .forms import *

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo-view')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(SignUpView, self).get(*args, **kwargs)


def logout(request):
    auth.logout(request)
    return redirect('login')
