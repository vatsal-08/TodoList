from django.urls import path
from .views import TodoView, TodoUpdateView, TodoDetailView, TodoCreateView, TodoDelete
from .views import delete_view
urlpatterns = [
    path('', TodoView.as_view(), name='todo-view'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='todo-detail'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='todo-update'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='todo-delete'),
    path('del/', delete_view, name='todos-delete')
]
