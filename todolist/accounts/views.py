from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic import CreateView


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo-view')


class SignUpView(FormView):
    template_name = 'todo/signin.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(SignUpView, self).get(*args, **kwargs)
