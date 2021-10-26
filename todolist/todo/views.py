from django.shortcuts import render

from .models import Todo
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class TodoView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo/todos.html'
    context_object_name = 'todos'
    login_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = context["todos"].filter(user=self.request.user)
        context["count"] = context["todos"].filter(status=False).count()
        return context


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'
    login_url = '/login/'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ["title", "description", "status"]
    success_url = reverse_lazy('todo-view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    login_url = '/accounts/login/'
    fields = ['title', 'description', 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
