from django.contrib import admin
from .models import Author, Quotes


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    pass
