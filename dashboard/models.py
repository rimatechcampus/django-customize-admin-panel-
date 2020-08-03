from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='topics')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='topics')
    created_dt = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    updated_by = models.ForeignKey(
        User, null=True, related_name='+', on_delete=models.CASCADE)
    updated_dt = models.DateTimeField(null=True)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(
        Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, null=True, related_name='+', on_delete=models.CASCADE)
