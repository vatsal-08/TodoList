from django.urls import path
from .views import TodoView, TodoUpdateView, TodoDetailView, TodoCreateView
urlpatterns = [
    path('', TodoView.as_view(), name='todo-view'),
    path('<int:pk>/detail', TodoDetailView.as_view(), name='todo-detail'),
    path('<int:pk>/update', TodoUpdateView.as_view(), name='todo-update'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),
]
