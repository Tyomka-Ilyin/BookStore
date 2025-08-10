from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.BuyView.as_view(), name='buy'),
    path('payed-online-order/', views.goBuy, name='goBuy'),
]