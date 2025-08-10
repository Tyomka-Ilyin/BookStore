import os

from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.db.models import F
from django.http import request, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from BookStore import settings
from Buy.models import Buy, structureBuy
from .models import *

from django import template

from .templatetags import tagsCatalog
from Cart.models import Cart, structureCart

from pprint import pprint

register = template.Library()

class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect("/")

class Catalog(View):
    def get(self, request, *args, **kwargs):
        books=Book.objects.all()

        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)

            structure = structureCart.objects.filter(cart=cart)

            buys = Buy.objects.filter(user=request.user)

            structureBuys = []

            for buy in buys:
                structureB = structureBuy.objects.filter(buy=buy)

                for str in structureB:
                    structureBuys.append(str)

            return render(request, 'catalog/catalog.html', {"books":books, "structure":structure, "buys":structureBuys})

        return render(request, 'catalog/catalog.html', {"books":books})


def detailBook(request, idBook):
    book = Book.objects.get(pk=idBook)

    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)

        structure = structureCart.objects.filter(cart=cart)

        buys = Buy.objects.filter(user=request.user)

        structureBuys = []

        for buy in buys:
            structureB = structureBuy.objects.filter(buy=buy)

            for str in structureB:
                structureBuys.append(str)

        return render(request, 'catalog/detailBook.html', {"book": book, "structure": structure, "buys":structureBuys})

    return render(request, 'catalog/detailBook.html', {"book": book})

def search(request):
    books=Book.objects.filter(title__contains=request.GET.get("titleBook"))

    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)

        structure = structureCart.objects.filter(cart=cart)

        buys = Buy.objects.filter(user=request.user)

        structureBuys = []

        for buy in buys:
            structureB = structureBuy.objects.filter(buy=buy)

            for str in structureB:
                structureBuys.append(str)

        return render(request, 'catalog/catalog.html', {"books": books, "structure": structure, "buys":structureBuys})

    return render(request, 'catalog/catalog.html', {"books": books})


def searchToGenre(request, idGenre):
    genre=Genre.objects.get(pk=idGenre)

    booksToGenre=BookGenre.objects.filter(Genre=genre)

    books=[]

    for item in booksToGenre:
        books.append(item.Book)

    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)

        structure = structureCart.objects.filter(cart=cart)

        buys = Buy.objects.filter(user=request.user)

        structureBuys = []

        for buy in buys:
            structureB = structureBuy.objects.filter(buy=buy)

            for str in structureB:
                structureBuys.append(str)

        return render(request, 'catalog/catalog.html', {"books": books, "structure": structure, "buys":structureBuys})

    return render(request, 'catalog/catalog.html', {"books": books})

def addToCartInCatalog(request, idBook):
    book=Book.objects.get(pk=idBook)
    user = request.user

    cart=Cart.objects.get(user=user)
    cart.sumCart=cart.sumCart+book.nds.priceWithNDS
    cart.save()

    strCart = structureCart(cart=cart, book=book)
    strCart.save()

    return HttpResponseRedirect("/")

def addToCartInDetailBook(request, idBook):
    book = Book.objects.get(pk=idBook)
    user = request.user

    cart = Cart.objects.get(user=user)
    cart.sumCart = cart.sumCart + book.nds.priceWithNDS
    cart.save()

    strCart = structureCart(cart=cart, book=book)
    strCart.save()

    return HttpResponseRedirect(reverse("detailBook", args=(book.id,)))

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="book/file")
            response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
            return response

    return Http404