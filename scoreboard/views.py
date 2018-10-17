from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class Scores(generic.ListView, LoginRequiredMixin):
    login_url = '/login/'
    models = models.scoreBoard
    template_name="scores.html"

    def get_queryset(self):
        return models.scoreBoard.objects.all()