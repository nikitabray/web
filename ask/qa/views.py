from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def mainpage(request):
    paginator = Paginator(Question.objects.new(), 10)
    page = request.GET.get('page', 1)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {'page': page, 'posts': page.object_list}
    return render(request, 'index.html', context)
