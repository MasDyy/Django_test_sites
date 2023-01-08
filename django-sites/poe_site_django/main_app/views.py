from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseNotFound
from .models import *

main_menu = ['Главная страница', 'Метовые билды', 'Лиг-стартеры']


def index(request):
    starters = StarterListDescription.objects.all()
    return render(
        request, 'main_app/base.html',
        {'starters': starters,
         'title': 'Главная страница',
         'main_menu': main_menu
         }
    )


def detail(request, id_char):
    char_404 = get_list_or_404(StarterListDescription, pk=id_char)
    return render(request, 'main_app/detail.html', {'char_404': char_404})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1')
