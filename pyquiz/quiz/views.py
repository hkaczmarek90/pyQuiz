from django.contrib import messages
from django.shortcuts import (
    render,
    redirect
)

from pyquiz.quiz.models import (
    Quiz,
    Question,
    Test,
    TestResult
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
    return redirect('question_new', id=quiz.id)


def quizzes(request):
    if request.user.is_authenticated:
        quizzes = Quiz.objects.all()
        return render(request, 'quizzes.html', {'quizzes': quizzes})
    quizzes = Quiz.objects.filter(public=True)
    return render(request, 'quizzes.html', {'quizzes': quizzes})


def save_question(request, id):
    question = QuestionForm(request.POST)
    if request.user.is_authenticated:
        if question.is_valid():
            question = question.save(commit=False)
            question.created_by = request.user
            question.quiz = Quiz.objects.get(pk=id)
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


def add_question(request, id):
    quiz = Quiz.objects.get(pk=id)
    form = QuestionForm(instance=quiz)
    return render(request, 'add_question.html', {"form": form, 'quiz': quiz})


def save_answer(request, id):
    question = Question.objects.get(pk=id)
    if request.method == 'POST':
        formset = AnswerFormset(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
        else:
            return redirect('home')
    return redirect('add_answer', id=question.id)


def start_test(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.all()

    test = Test.objects.create(quiz=quiz, user=request.user)
    if request.user.is_authenticated:

        test.save()

    else:
        messages.add_message(request, messages.INFO, 'Please Sign In To Continue This Action')

    return render(request, 'start_test.html', {'questions': questions,
                                               'test': test})


def show_test_result(request, test_result_id):
    test_result = TestResult.objects.get(pk=test_result_id)
    percent_test_score = int(test_result.correct_answer / (test_result.correct_answer + test_result.wrong_answer) * 100)
    return render(request, 'test_result.html', {'test_result': test_result,
                                                'percent_test_score': percent_test_score})
