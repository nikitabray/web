from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login 
from .models import *
from .forms import *


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def mainpage(request):
    paginator = Paginator(Question.objects.new(), 10)
    page = request.GET.get('page', 1)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {'page': page, 'posts': page.object_list}
    return render(request, 'index.html', context)


def popular(request):
    paginator = Paginator(Question.objects.popular(), 10)
    page = request.GET.get('page', 1)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {'page': page, 'posts': page.object_list}
    return render(request, 'index.html', context)


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    answer = Answer.objects.filter(question=question)
    context = {'question': question, 'answer': answer}
    return render(request, 'question.html', context)


def postform(request):
    if request.method == 'POST':
        form = AskForm(request.user, request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect('/question/' + str(question.id))
    else:
        form = AskForm(request.user)
    return render(request, 'add_post.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user = authenticate(username=username, password=password)
        print('user is ', user)
        if user:
            login(request, user)
        response = HttpResponseRedirect('home')
        if not request.session.session_key:
            request.session.save()
        print(request.session.session_key)
        response.set_cookie('sessionid', request.session.session_key)       
        return response
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

def login_to_site(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        # if form.is_valid():
        #     print('AHAHEHDS;LDKAFLMF;AM')
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('HAHAHAHAHHA', user)
            login(request, user)
        response = HttpResponseRedirect('home')
        if not request.session.session_key:
            request.session.save()
        response.set_cookie('sessionid', request.session.session_key) 
        print(request.session.get('session_key'))
        return response
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
