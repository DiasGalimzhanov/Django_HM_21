from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    class TodoStatus(models.TextChoices):
        C = 'C', 'Created'
        P = 'P', 'Processed'
        D = 'D', 'Done'
        
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=TodoStatus.choices,default=TodoStatus.C)
    deadline = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title