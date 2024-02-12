# определить классы  RegistrationForm и LoginForm
# С задания: создать формы RegistrationForm и LoginForm для ввода данных (логин, пароль, подтверждение пароля)

# forms.py
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')