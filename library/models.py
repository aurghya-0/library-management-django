from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    author_bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Patreon(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    call_id = models.CharField(max_length=20)
    book_name = models.CharField(max_length=200)
    book_author = models.ManyToManyField(Author)
    book_description = models.TextField(max_length=2000)

    def __str__(self):
        return self.book_name


class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patreon = models.ForeignKey(Patreon, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
