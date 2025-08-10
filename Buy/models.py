from django.contrib.auth.models import User
from django.db import models

from Catalog.models import Book


class Buy(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime=models.DateTimeField('Время покупки')
    sumBuy=models.DecimalField('Сумма покупки',decimal_places=2, max_digits=9)

    class Meta:
        verbose_name='Покупка'
        verbose_name_plural='Покупки'

    def __str__(self):
        return self.user.username

class structureBuy(models.Model):
    buy=models.ForeignKey(Buy, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Состав покупки'
        verbose_name_plural='Составы покупок'

    def __str__(self):
        return str(self.buy.id)

class discount(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    amounDiscount=models.DecimalField("Размер скидки",decimal_places=2, max_digits=9)

    class Meta:
        verbose_name='Скидка'
        verbose_name_plural='Скидки'

    def __str__(self):
        return str(self.buy.user.username)