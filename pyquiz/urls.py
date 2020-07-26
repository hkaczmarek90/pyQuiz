from django.contrib import admin
from django.urls import path, include

from pyquiz import views
from pyquiz.user.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('user/quizzes/', views.quizzes, name='quizzes'),
    path('quiz/add/', views.create_quiz, name='create_quiz'),
    path('quiz/save/', views.save_quiz, name='save_quiz'),
    path('user/quizzes/', views.quizzes, name='quizzes'),
    path('question/new', views.add_question, name='question_new'),
    path('question/save/', views.save_question, name='save_question'),
]

