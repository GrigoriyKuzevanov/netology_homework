from django.shortcuts import render
from .models import Book


def index(request):
    template = 'books/index.html'
    context = {}
    return render(request, template, context)


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def book_by_date_view(request, pub_date):
    template = 'books/book_pagi.html'
    books = Book.objects.filter(pub_date=pub_date)
    prev = Book.objects.filter(pub_date__lt=pub_date).values('pub_date').first()
    next = Book.objects.filter(pub_date__gt=pub_date).values('pub_date').first()
    context = {
        'books': books,
        'prev': prev,
        'next': next,
    }
    return render(request, template, context)