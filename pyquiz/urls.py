from django.contrib import admin
from django.urls import path, include
from pyquiz import views
from pyquiz.quiz import views as quiz_views
from pyquiz.user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('question/<int:id>/answer/add/', quiz_views.add_answer, name='add_answer'),
    path('question/<int:id>/answer/save/', quiz_views.save_answer, name='save_answer'),
    path('user/quizzes/', quiz_views.quizzes, name='quizzes'),
    path('quiz/add/', quiz_views.create_quiz, name='create_quiz'),
    path('quiz/save/', quiz_views.save_quiz, name='save_quiz'),
    path('user/quizzes/', quiz_views.quizzes, name='quizzes'),
    path('quiz/<int:id>/question/new/', quiz_views.add_question, name='question_new'),
    path('quiz/<int:id>/question/save/', quiz_views.save_question, name='save_question'),
    path('test/<int:quiz_id>/', quiz_views.start_test, name='start_test'),
    path('result/test/<int:test_result_id>/', quiz_views.show_test_result, name='test_result'),
]

