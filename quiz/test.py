from django.test import TestCase
from .models import Question
from django.contrib.auth.models import User


class ModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('test', 'test@gmail.com', 'testpass')
        Question.objects.create(value='Who created?', public=True, created_by= user)

    def test_question(self):
        question = Question.objects.get(value='Who created?')
        self.assertEqual(question.value, 'Who created?')
