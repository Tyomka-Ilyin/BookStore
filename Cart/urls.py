from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.CartView.as_view(), name='cart'),
    path('del/<int:idBook>', views.delBook, name='deleteBook'),
    path('buy/', include('Buy.urls')),
]