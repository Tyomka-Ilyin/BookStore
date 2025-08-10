from django import forms
from django.contrib.auth.models import User


class changeDetailUserForm(forms.ModelForm):
    email=forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Имя пользователя'
        self.fields['first_name'].label = 'Фамилия'
        self.fields['last_name'].label = 'Имя'
        self.fields['email'].label = 'Электронная почта'

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Данная почта уже зарегистрированна в системе")

        return email

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
