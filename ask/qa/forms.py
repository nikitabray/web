from django import forms
from .models import *

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', ]

    def clean(self):
        return self.cleaned_data

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question', ]
