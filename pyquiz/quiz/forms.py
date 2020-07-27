from django import forms
from django.forms import ModelForm

from pyquiz.quiz.models import (
    Question,
    Quiz,
    Answer
)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['value', 'public']


class AnswerForm1(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['value', 'correct']


class AnswerForm2(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['value', 'correct']


class AnswerForm3(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['value', 'correct']


class AnswerForm4(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['value', 'correct']


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'public', 'description']
