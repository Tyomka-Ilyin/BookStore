from django.http import HttpResponseRedirect
from django.urls import reverse

from Cart.models import Cart, structureCart
from django.shortcuts import render
from django.views.generic.base import View

from Catalog.models import Book


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)

        structure = structureCart.objects.filter(cart=cart)

        return render(request, 'cart/cart.html', {"structure": structure, "cart":cart})

def delBook(request, idBook):
    book=Book.objects.get(pk=idBook)

    cart = Cart.objects.get(user=request.user)
    cart.sumCart=cart.sumCart-book.nds.priceWithNDS
    cart.save()

    bookInStructure=structureCart.objects.get(cart=cart, book=book)
    bookInStructure.delete()

    return HttpResponseRedirect(reverse('cart'))

