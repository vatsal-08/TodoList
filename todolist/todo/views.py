from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from django.urls.base import reverse
from .forms import CreateViewForm
from .models import Todo
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class TodoView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo/todos.html'
    context_object_name = 'todos'
    login_url = 'accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = context["todos"].filter(user=self.request.user)
        context["total"] = context["todos"].count()
        context["count"] = context["todos"].filter(status=False).count()
        return context


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'
    login_url = 'accounts/login/'
    context_object_name = 'task'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'status']
    template_name = 'todo/todo_create.html'
    success_url = reverse_lazy('todo-view')
    login_url = 'accounts/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'todo/todo_update.html'
    login_url = 'accounts/login/'
    fields = ['description', 'status']
    context_object_name = 'task'
    # success_url = reverse_lazy('todo-view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('todo-detail', kwargs={'pk': self.kwargs['pk']})


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('todo-view')
    login_url = 'accounts/login/'
    template_name = 'todo/todo_delete.html'


def delete_view(self):
    Todo.objects.all().filter(status=True).delete()
    return HttpResponseRedirect("/")
