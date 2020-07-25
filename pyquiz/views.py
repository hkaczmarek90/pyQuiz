from django.shortcuts import render
from pyquiz.quiz.models import Quiz
from pyquiz.quiz.forms import QuizForm


def home(request):
    return render(request, 'home.html')


def create_quiz(request):
    return render(request, 'quiz_add.html', {'form': QuizForm()})


def profile_side(request):
    return render(request, 'profile_side.html', {'user': request.user})


def quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes.html', {'quizzes': quizzes})
