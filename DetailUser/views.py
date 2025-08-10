from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Cart.models import Cart, structureCart
from django.views.generic.base import View

from DetailUser.forms import changeDetailUserForm

from Buy.models import Buy, structureBuy
from DetailUser.models import Bonus


class DetailUser(View):
    def get(self, request, *args, **kwargs):
        user=request.user

        cart=Cart.objects.get(user=user)

        structure=structureCart.objects.filter(cart=cart)

        bonus=Bonus.objects.get(user=user)

        buys=Buy.objects.filter(user=user)

        structureBuys=[]

        for buy in buys:
            structureB = structureBuy.objects.filter(buy=buy)

            for str in structureB:
                structureBuys.append(str)

        return render(request, "detailUser/detailUser.html", {"user":user, "structure": structure, "bonus": bonus,
                                                               "structureBuys": structureBuys})

class ChangeDetailUserView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        data={'username': user.username, 'password': user.password, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
        form = changeDetailUserForm(data)

        cart = Cart.objects.get(user=user)
        structure = structureCart.objects.filter(cart=cart)

        return render(request, "detailUser/changeDetailUser.html", {"user":user, "structure": structure, "form":form})

    def post(self, request, *args, **kwargs):
        form = changeDetailUserForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user=request.user
            user.username=username
            user.email=email
            user.first_name=first_name
            user.last_name=last_name
            user.save()

            return HttpResponseRedirect('/')

        context = {'form': form}
        return render(request, 'registration/registration.html', context)