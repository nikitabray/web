from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class AskForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AskForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Question
        fields = [
            'title',
            'text',
        ]

    def clean(self):
        self.cleaned_data['author'] = User.objects.get(id=self.user)
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'text',
            'question',
        ]


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        User.objects.create_user(self.cleaned_data['username'],
                                 self.cleaned_data['email'],
                                 self.cleaned_data['password'])


# class SignUpForm(forms.Form):
#     password = forms.CharField(label=("Password"),
#         widget=forms.PasswordInput)
#     password1 = password
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
