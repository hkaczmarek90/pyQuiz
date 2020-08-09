from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import (
    render,
    redirect
)

from pyquiz.quiz.models import (
    Quiz,
    Answer,
    Question,
    Test,
    TestResult
)

from pyquiz.quiz.forms import (
    QuizForm,
    QuestionForm,
    AnswerFormset,
)


@login_required
def create_quiz(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You Must Be Logged To Use This Function')
        return redirect('home')

    form = QuizForm()
    return render(request, 'quiz_add.html', {'form': form})


@login_required
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


@login_required
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


@login_required
def add_answer(request, id):
    question = Question.objects.get(pk=id)
    formset = AnswerFormset(instance=question)
    return render(request, 'add_answer.html', {'formset': formset,
                                               'question': question})


@login_required
def add_question(request, id):
    quiz = Quiz.objects.get(pk=id)
    form = QuestionForm(instance=quiz)
    return render(request, 'add_question.html', {"form": form, 'quiz': quiz})


@login_required
def save_answer(request, id):
    question = Question.objects.get(pk=id)
    if request.method == 'POST':
        formset = AnswerFormset(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
        else:
            return redirect('home')
    return redirect('add_answer', id=question.id)


@login_required
def start_test(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz_id)

    test = Test.objects.create(quiz=quiz, user=request.user)
    if request.user.is_authenticated:

        test.save()

    else:
        messages.add_message(request, messages.INFO, 'Please Sign In To Continue This Action')

    return render(request, 'start_test.html', {'questions': questions,
                                               'test': test})


def results_save(request, test_id):
    test = Test.objects.get(pk=test_id)
    answers = list(request.POST.values())

    correct_answers = Answer.objects.filter(correct=True).filter(pk__in=answers).count()

    test_results = TestResult(wrong_answer=len(answers) - correct_answers, correct_answer=correct_answers,
                              test=test)
    test_results.save()

    return render(request, "home.html")


def show_test_result(request, test_result_id):
    test_result = TestResult.objects.get(pk=test_result_id)
    percent_test_score = int(test_result.correct_answer / (test_result.correct_answer + test_result.wrong_answer) * 100)

    if percent_test_score < 30:
        result_comment = "Mogło byś lepiej"
    elif 30 < percent_test_score < 70:
        result_comment = "Całkiem dobrze"
    else:
        result_comment = "Świetny wynik"
    return render(request, 'test_result.html', {'test_result': test_result,
                                                'percent_test_score': percent_test_score,
                                                'result_comment': result_comment})
