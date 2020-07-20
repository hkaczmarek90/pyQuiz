from django.shortcuts import render
from quiz.models import Quiz


def quizzes(request):
    quizzes = Quiz.objects.all()

    return render(request, 'quizzes.html', {'quizzes': quizzes})
