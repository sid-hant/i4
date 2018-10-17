from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse_lazy, reverse

# Create your models here.
register = template.Library()
User = get_user_model()

class Upload(models.Model):
    user = models.ForeignKey(User, related_name="b", on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    file1 = models.FileField(upload_to="submissions",blank=True)
    file2 = models.FileField(upload_to="submissions",blank=True)
    file3 = models.FileField(upload_to="submissions",blank=True)
    file4 = models.FileField(upload_to="submissions",blank=True)
    file5 = models.FileField(upload_to="submissions",blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
