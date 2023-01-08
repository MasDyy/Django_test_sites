from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

from .models import *
# Create your views here.
menu = ['Меню', 'Открыть', 'Закрыть', 'Удалить', 'Выйти']


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, cat):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    elif int(year) == 2666:
        raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')




