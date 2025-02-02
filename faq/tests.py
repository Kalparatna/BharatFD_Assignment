from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a Python framework.")

    def test_translation(self):
        self.assertTrue(self.faq.question_hi)
        self.assertTrue(self.faq.question_bn)
