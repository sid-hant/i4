from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth import get_user_model
# Create your views here.

class PostList(generic.ListView):
    models = models.Posts
    template_name="posts.html"

    def get_queryset(self):
        return models.Posts.objects.filter(user=self.request.user)

class Score(generic.ListView):
    models = models.Posts
    template_name="scoreboard.html"

    def get_queryset(self):
        return models.Posts.objects.filter(post_id=1)
