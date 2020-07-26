from django.shortcuts import (
    render,
    redirect
)
from pyquiz.user.models import User
from pyquiz.quiz.models import Quiz
from pyquiz.quiz.forms import QuizForm
from pyquiz.quiz.forms import QuestionForm


def home(request):
    return render(request, 'home.html')


def create_quiz(request):
    form = QuizForm()
    return render(request, 'quiz_add.html', {'form': form})


def save_quiz(request):
    request.methods = 'POST'
    form = QuizForm(request.POST)
    if request.user.is_authenticated:
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
        else:
            return redirect('home')
    else:
        return redirect('home')
    return render(request, 'home.html', {'form': form})


def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes.html', {'quizzes': quizzes})


def add_question(request):
    question = QuestionForm()
    return render(request, 'add_question.html', {'form': question})


def save_question(request):
    request.methods = 'POST'
    form = QuestionForm(request.POST)
    if request.user.is_authenticated:
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
        else:
            return redirect('home')
    else:
        return redirect('home')
    return render(request, 'home.html', {'form': form})
