from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import request, HttpResponseRedirect


from Catalog.models import Book

from .forms import RegistrationForm, InputForm
from Cart.models import Cart

from DetailUser.models import Bonus


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        books = Book.objects.all()
        context = {'form': form, 'books':books}

        return render(request, 'registration/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            newUser = User.objects.create_user(username=form.cleaned_data['username'],
                                               email=form.cleaned_data['email'],
                                               first_name=form.cleaned_data['first_name'],
                                               last_name=form.cleaned_data['last_name'],
                                               password=form.cleaned_data['password'])

            new_Cart = Cart(user=newUser, sumCart=0)
            new_Cart.save()

            new_Bonus = Bonus(user=newUser, kolBonus=0)
            new_Bonus.save()

            user=authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')

        context={'form': form}
        return render(request, 'registration/registration.html', context)

class InputView(View):

    def get(self, request, *args, **kwargs):
        form = InputForm(request.POST or None)
        context = {'form': form}

        return render(request, 'input/input.html', context)

    def post(self, request, *args, **kwargs):
        form = InputForm(request.POST or None)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')

        context={'form': form}
        return render(request, 'input/input.html', context)