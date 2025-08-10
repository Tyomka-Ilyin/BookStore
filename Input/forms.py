from django import forms
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Имя пользователя'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['first_name'].label = 'Фамилия'
        self.fields['last_name'].label = 'Имя'
        self.fields['email'].label = 'Электронная почта'

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Данное имя пользователя уже зарегистрированно в системе")

        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Данная почта уже зарегистрированна в системе")

        try:
            message = EmailMessage(
                'Сообщение от онлайн-магазина "Умная книга"', 'Спасибо за регистрацию в нашем интернет-магазине',
                'bookstore2000@mail.ru',
                [email])

            message.send()

            return email
        except Exception as ex:
            raise forms.ValidationError(f"Такой почты не существует"+str(ex))

    def clean_password(self):
        password = self.cleaned_data['password']

        if User.objects.filter(password=password).exists():
            raise forms.ValidationError(f"Извините, пароль занят")

        return password

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password!=confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email',]


class InputForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Имя пользователя'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username=self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Неверное имя пользователя')

        user=User.objects.filter(username=username).first()

        if user:
            if not user.check_password(password):
                raise forms.ValidationError(f'Неверный пароль')

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
