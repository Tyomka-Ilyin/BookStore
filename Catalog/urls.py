from django.contrib.auth.views import LogoutView
from django.urls import path, include, re_path
from django.views.static import serve

from BookStore import settings
from . import views

app_name=''

urlpatterns=[
    path('', views.Catalog.as_view(), name="showCatalog"),
    path('search/', views.search, name='search'),
    path('input/', include('Input.urls')),
    path('book/<int:idBook>', views.detailBook, name='detailBook'),
    path('genre/<int:idGenre>', views.searchToGenre, name='genre'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('addToCartInCatalog/<int:idBook>', views.addToCartInCatalog, name='addToCartInCatalog'),
    path('cart/', include('Cart.urls')),
    path('addToCartInDetailBook/<int:idBook>', views.addToCartInDetailBook, name='addToCartInDetailBook'),
    path('detailUser/', include('DetailUser.urls')),
    re_path(r'^download/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT})
]