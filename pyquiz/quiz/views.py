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

    else:
        form = QuizForm()
        messages.add_message(request, messages.INFO, 'Welcome. Now You Can Create Your Own Quizz.')
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
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO,
                             'Welcome To Our Site. Now You Are Logged Out. You Can Only Use Our Public Quizzes. To Use Personal Quizzes Please Logg In.')
        quizzes = Quiz.objects.all()
        return render(request, 'quizzes.html', {'quizzes': quizzes})
    else:

        quizzes = Quiz.objects.filter(public=True)
        messages.add_message(request, messages.INFO,
                             'Welcome To Our Site. You Are Already Logged In. You Can Use Both Public And Personal Quizzes.')
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
    messages.add_message(request, messages.INFO, 'Your Added New Question.')
    return render(request, 'add_answer.html', {'formset': formset,
                                               'question': question})


def add_question(request, id):
    quiz = Quiz.objects.get(pk=id)
    form = QuestionForm(instance=quiz)
    messages.add_message(request, messages.INFO, 'Now You Can Add New Question.')
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
    result_comment = ""
    if percent_test_score < 30:
        result_comment = "Mogło byś lepiej"
    elif 30 < percent_test_score < 70:
        result_comment = "Całkiem dobrze"
    else:
        result_comment = "Świetny wynik"
    return render(request, 'test_result.html', {'test_result': test_result,
                                                'percent_test_score': percent_test_score,
                                                'result_comment': result_comment})
