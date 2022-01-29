from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=150)
    date_birthday = models.CharField(max_length=150)
    about = models.TextField()

    def get_absolute_url(self):
        return reverse('authors_info', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'


class Quotes(models.Model):
    quotes = models.CharField(max_length=5000)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quotes}'
