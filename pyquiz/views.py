from django.contrib import messages
from django.shortcuts import (
    render,
    redirect
)

from pyquiz.quiz.models import Quiz
from pyquiz.quiz.forms import QuizForm
from pyquiz.quiz.forms import QuestionForm


def home(request):
    return render(request, 'home.html')


def create_quiz(request):
    form = QuizForm()
    return render(request, 'quiz_add.html', {'form': form})


def save_quiz(request):
    form = QuizForm(request.POST)
    if request.user.is_authenticated:
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
        else:
            return redirect('home')
    else:
        messages.add_message(request, messages.INFO, 'Please Sign In To Continue This Action')

        return redirect('home')
    return render(request, 'home.html', {'form': form})


def quizzes(request):
    if request.user.is_authenticated:
        quizzes = Quiz.objects.all()
        return render(request, 'quizzes.html', {'quizzes': quizzes})
    quizzes = Quiz.objects.filter(public=True)
    return render(request, 'quizzes.html', {'quizzes': quizzes})
  

def add_question(request):
    return render(request, 'add_question.html', {'form': QuestionForm()})


def save_question(request):
    question = QuestionForm(request.POST)
    if request.user.is_authenticated:
        if question.is_valid():
            question = question.save(commit=False)
            question.created_by = request.user
            question.save()
        else:
            return redirect('home')
    else:
        messages.add_message(request, messages.INFO, 'Please Sign In To Continue This Action')
    return render(request, 'home.html', {'form': question})
