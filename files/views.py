from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class FilesList(generic.ListView, LoginRequiredMixin):
    login_url = '/login/'
    models = models.Files
    template_name="files.html"

    def get_queryset(self):
        return models.Files.objects.filter(Q(close_time__gte=timezone.now()) & Q(open_time__lte=timezone.now()))
