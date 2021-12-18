from django import forms
from todo.models import Todo


class CreateViewForm(forms.Form):

    class Meta:
        model = Todo
        fields = ['title', 'description', 'status']
        
