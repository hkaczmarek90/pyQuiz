from django.db import models


class Question(models.Model):
    value = models.TextField()
    public = models.BooleanField()
    created_by = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value


class Answer(models.Model):
    value = models.TextField()
    correct = models.BooleanField()
    question_id = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.value
