from django.db import models


class Question(models.Model):
    value = models.TextField()
    public = models.BooleanField()
    created_by = models.ForeignKey('auth.User', on_delete=models.SET('u_removed'))

    def __str__(self):
        return self.value


class Quiz(models.Model):
    name = models.TextField()
    public = models.BooleanField()
    description = models.TextField()
    created_by = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
