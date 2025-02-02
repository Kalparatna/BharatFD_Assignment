from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache
import asyncio

LANGUAGES = ['hi', 'bn', ]

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  
    question_bn = models.TextField(blank=True, null=True)  

    async def translate_text(self, text, dest):
        """Translate text asynchronously."""
        translator = Translator()
        translation = await translator.translate(text, src="en", dest=dest)
        return translation.text

    def save(self, *args, **kwargs):
        """Ensure translations are set before saving."""
        if self.question and not self.question_hi:
            self.question_hi = asyncio.run(self.translate_text(self.question, "hi"))
        if self.question and not self.question_bn:
            self.question_bn = asyncio.run(self.translate_text(self.question, "bn"))

        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        """Retrieve translated question with caching."""
        cache_key = f'faq_{self.id}_question_{lang}'
        cached_question = cache.get(cache_key)
        if cached_question:
            return cached_question

        if lang == 'hi':
            question = self.question_hi or self.question
        elif lang == 'bn':
            question = self.question_bn or self.question
        else:
            question = self.question

        cache.set(cache_key, question, timeout=3600)
        return question