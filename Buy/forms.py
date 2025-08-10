from datetime import datetime

from django import forms
from django.db import models
from django.contrib.auth.models import User


class detBuy(models.Model):
    bonus = models.IntegerField()

class BuyForm(forms.ModelForm):
    bonus=forms.CharField(widget=forms.NumberInput, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bonus'].label = 'Потратить бонусов'

    class Meta:
        model = detBuy
        fields = ['bonus']