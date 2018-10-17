from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from .forms import Submit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def getForm(request):
    form = Submit()
    if request.method == "POST":
        form = Submit(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            message = form.cleaned_data['message']
            file1 = form.cleaned_data['file1'] 
            file2 = form.cleaned_data['file2']
            file3 = form.cleaned_data['file3']
            file4 = form.cleaned_data['file4']
            file5 = form.cleaned_data['file5']

            return render(request, "submissions.html", {'form':form})
    return render(request, "submissions.html", {'form': form})