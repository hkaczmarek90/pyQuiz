"""pyquiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from pyquiz import views
from pyquiz.user.views import signup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quiz/add/', views.create_quiz, name='create_quiz'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_side, name='profile_side'),
    path('user/quizzes/', views.quizzes, name='quizzes')
    path('accounts/profile/', views.profile, name='profile_side'),
    path('user/quizzes/', views.quizzes, name='quizzes'),
    path('signup/', signup, name='signup'),
]