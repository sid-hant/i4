from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse_lazy, reverse

# Create your models here.
User = get_user_model()

class Files(models.Model):
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    title = models.TextField(null=True)
    message = models.TextField()
    files = models.FileField(upload_to="files", blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-close_time']
