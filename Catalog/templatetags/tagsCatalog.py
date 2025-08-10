from django import template

from Catalog.models import Genre, Book
from django.http import request

from Cart.models import structureCart

register = template.Library()

@register.simple_tag()
def getGenres():
    genres = Genre.objects.all()

    return genres

@register.simple_tag()
def getBooks():
    books = Book.objects.all()

    return books

@register.simple_tag()
def setBook(structure):
    books = []

    for i in structure:
        books.append(i.book.title)

    return books

@register.simple_tag()
def setBuysBook(buys):
    books=[]

    for item in buys:
        books.append(item.book.title)

    return books
