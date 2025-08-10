from django.contrib.auth.models import User
from django.db import models

from Catalog.models import Book


class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    sumCart = models.DecimalField("Сумма корзины", decimal_places=2, max_digits=9)

    class Meta:
        verbose_name='Корзина'
        verbose_name_plural='Корзины'

    def __str__(self):
        return self.user.username

class structureCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Состав корзины'
        verbose_name_plural='Составы корзин'

    def __str__(self):
        return str(self.cart.id)