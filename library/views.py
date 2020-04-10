from django.shortcuts import render
from .models import Book


def library_home(request):
    return render(request, 'library/library_home.html')


def library_books(request):
    books = Book.objects.all()
    return render(request, 'library/library_books.html', {'books': books})
