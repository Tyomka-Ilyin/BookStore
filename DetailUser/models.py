from django.contrib.auth.models import User
from django.db import models

class Bonus(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    kolBonus=models.IntegerField("Количество бонусов")

    class Meta:
        verbose_name='Бонусы'
        verbose_name_plural='Бонусы пользователей'

    def __str__(self):
        return str(self.user.username)