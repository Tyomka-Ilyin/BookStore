from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.DetailUser.as_view()),
    path('changeDetailUser/', views.ChangeDetailUserView.as_view(), name='changeDetailUser')
]