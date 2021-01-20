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


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

# class SignUpForm(forms.Form):
#     password = forms.CharField(label=("Password"),
#         widget=forms.PasswordInput)
#     password1 = password
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')



