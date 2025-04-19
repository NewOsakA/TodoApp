from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Todo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True, folder='todo_images/')

    def __str__(self):
        return self.title
