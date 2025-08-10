from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.InputView.as_view(), name='input'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]