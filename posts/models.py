from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
import misaka
from django import template
from django.urls import reverse_lazy, reverse

# Create your models here.
register = template.Library()
User = get_user_model()

class Posts(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    post_id = models.IntegerField(null=True)
    message = models.TextField()
    image = models.ImageField(upload_to="post-pics",blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
