from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import get_user_model
from django.views import generic
