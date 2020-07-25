from django.forms import ModelForm

from pyquiz.quiz.models import Quiz


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
