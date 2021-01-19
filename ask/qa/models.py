from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_user', default=1)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    class Meta:
        verbose_name = 'Question'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('question', kwargs={'question_id': self.pk})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_user')
