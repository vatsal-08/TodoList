from django.db import models


class Todo(models.Model):
    description = models.TextField()
    time = models.DateTimeField(auto_now=True)
