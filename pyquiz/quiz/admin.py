from django.contrib import admin

from pyquiz.quiz.models import Question, Answer, Quiz, UserAnswer, Test

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Test)
admin.site.register(UserAnswer)
