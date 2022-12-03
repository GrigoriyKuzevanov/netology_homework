import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvf:
    reader = csv.DictReader(csvf)


def bus_stations(request):
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
        content = list(reader)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
