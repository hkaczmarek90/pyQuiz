from django.db import models
from django.conf import settings
from pyquiz.user.models import User


class Question(models.Model):
    value = models.TextField()
    public = models.BooleanField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value


class Answer(models.Model):
    value = models.TextField()
    correct = models.BooleanField()
    question_id = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value


class Quiz(models.Model):
    name = models.TextField()
    public = models.BooleanField()
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Test(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    test = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
