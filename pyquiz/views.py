from django.shortcuts import render

from pyquiz.quiz.models import Quiz


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile_side.html', {'user': request.user})


def quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes.html', {'quizzes': quizzes})
