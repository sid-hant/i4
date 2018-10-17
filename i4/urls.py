"""i4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from posts import views as post_views
from files import views as file_views
from django.conf import settings
from django.conf.urls.static import static
from uploads import views as upload_views
from scoreboard import views as score_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p/', login_required(post_views.PostList.as_view(),login_url='login'), name='posts'),
    path('f/', login_required(file_views.FilesList.as_view(),login_url='login'), name='files'),
    path('u/', login_required(upload_views.getForm,login_url='login'), name='uploads'),
    path('s/', login_required(score_views.Scores.as_view(),login_url='login'), name='scores'),
    path('', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login'),
    path('logout/', login_required(auth_views.LogoutView.as_view(),login_url='login'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

