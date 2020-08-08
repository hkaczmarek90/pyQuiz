from django.contrib import messages
from django.shortcuts import (
    render,
    redirect
)

from pyquiz.quiz.models import (
    Quiz,
    Question,
)

from pyquiz.quiz.forms import (
    QuizForm,
    QuestionForm,
    AnswerFormset,
)


def create_quiz(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You Must Be Logged To Use This Function')
        return redirect('home')

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
    return render(request, 'add_question.html', {'form': form})


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
    return redirect('add_answer', id=question.id)


def add_answer(request, id):
    question = Question.objects.get(pk=id)
    formset = AnswerFormset(instance=question)
    return render(request, 'add_answer.html', {'formset': formset,
                                               'question': question})


def save_answer(request, id):
    question = Question.objects.get(pk=id)
    if request.method == 'POST':
        formset = AnswerFormset(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
        else:
            return redirect('home')
    return redirect('add_answer', id=question.id)
