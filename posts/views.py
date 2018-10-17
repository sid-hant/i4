from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class PostList(generic.ListView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'posts.html'
    models = models.Posts
    template_name="posts.html"

    def get_queryset(self):
        return models.Posts.objects.filter(Q(user=self.request.user) | Q(showEveryone=True))


