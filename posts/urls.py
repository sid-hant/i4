from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

app_name = 'posts'

urlpatterns = [
  #  path('posts/', views.PostList.as_view(), name='ann'),
  #  path('score/', views.Score.as_view(), name='score')
]
