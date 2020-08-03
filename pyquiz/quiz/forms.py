from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from pyquiz.quiz.models import (
    Question,
    Quiz,
    Answer,
)


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['value', 'public']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['value', 'correct']


AnswerFormset = inlineformset_factory(Question, Answer, fields=('value', 'correct',), extra=3, max_num=4)


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'public', 'description']
