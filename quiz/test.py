from django.test import TestCase
from .models import Question


class ModelTest(TestCase):
    def setUp(self):
        Question.objects.create(value='Who created?', public=True, created_by='test')

    def test_question(self):
        test_question = Question.objects.get(value='Who created?')
        self.assertEqual(test_question, 'Who created?')
