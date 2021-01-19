from django import forms
from .models import *

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'author']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question', 'author']
