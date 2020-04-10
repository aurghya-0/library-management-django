from django.contrib import admin
from .models import Author, Book, Patreon, BookIssue

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Patreon)
admin.site.register(BookIssue)
