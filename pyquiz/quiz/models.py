from django.db import models
from django.conf import settings
from pyquiz.user.models import User


class Question(models.Model):
    value = models.CharField(max_length=256)
    public = models.BooleanField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value


class Answer(models.Model):
    value = models.CharField(max_length=256)
    correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    public = models.BooleanField()
    description = models.CharField(max_length=256, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Test(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class UserAnswer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer_id = models.ForeignKey(Answer, on_delete=models.DO_NOTHING)
    test_id = models.ForeignKey(Test, on_delete=models.DO_NOTHING)


class TestResult(models.Model):
    correct_answer = models.IntegerField(default=0)
    wrong_answer = models.IntegerField(default=0)
    test_id = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
