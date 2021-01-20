from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class SignUpForm(UserCreationForm):
    password = super().password1
    class Meta:
        model = User
        fields = ('username', 'email', 'password')



