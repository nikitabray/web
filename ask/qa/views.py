from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
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
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect('/question/' + str(question.id))
    else:
        form = AskForm()
    return render(request, 'add_post.html', {'form': form})
