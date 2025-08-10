from django import forms

class ReportForm(forms.Form):
    dateStart = forms.DateField(label='Начало периода')
    dateEnd = forms.DateField(label='Конец периода')