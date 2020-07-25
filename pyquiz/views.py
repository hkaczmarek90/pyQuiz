from django.shortcuts import render
from django.forms import modelformset_factory

from pyquiz.quiz.models import Quiz
from pyquiz.quiz.forms import QuizForm


def home(request):
    return render(request, 'home.html')


def create_quiz(request):
    form = QuizForm()
    return render(request, 'quiz_add.html', {'form': form})


def save_quiz(request):
    request.methods = 'POST'
    form = QuizForm(request.POST)
    form.save()
    return render(request, 'home.html', {'form': form})


def profile(request):
    return render(request, 'profile_side.html', {'user': request.user})


def quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes.html', {'quizzes': quizzes})
