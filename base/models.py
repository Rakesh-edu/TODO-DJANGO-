from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title