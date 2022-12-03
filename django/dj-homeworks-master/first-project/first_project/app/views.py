from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time()
    msg = f"Текущее время: {current_time.strftime('%H:%M:%S')}"
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/workdirlist.html'
    dir_list = os.listdir()
    context = {
        'dir_list': dir_list
    }

    return render(request, template_name, context)
