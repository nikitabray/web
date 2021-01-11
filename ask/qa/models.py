from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=80)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    class Meta:
        verbose_name = 'Вопрос'
        order_by = ['-added_at']

    class QuestionManager(models.Manager):
        def new(self):
            return self.order_by('-added_at')

        def popular(self):
            return self.order_by('-rating')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
    )
    author = models.CharField(max_length=80)
