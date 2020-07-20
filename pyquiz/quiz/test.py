from django.test import TestCase
from pyquiz.quiz.models import Question
from django.contrib.auth.models import User


class QuestionTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test', 'test@test.pl', 'passtest')
        Question.objects.create(value="Who created?", public=True, created_by=user)

    def test_question_object(self):
        q1 = Question.objects.get(value='Who created?')
        self.assertEqual(q1.value, "Who created?")
