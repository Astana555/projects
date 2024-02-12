from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login
from .models import User, UserProfile
from .forms import RegistrationForm, LoginForm

# определите методы register_user() и login_user()
# добавить метод reset_password_via_email()
# (Реализовать метод reset_password_via_email() для восстановления пароля через электронную почту)

def bootstrap_page_handler(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                user = User.objects.create(username=username, password=password)
                UserProfile.objects.create(user=user)
                return redirect('index')
            else:
                # Обработка ошибки при несовпадении паролей
                pass
    else:
        form = RegistrationForm()

    return render(request, 'registration_page.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Используем стандартную функцию authenticate для аутентификации пользователя
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')  # Заменила 'dashboard' на основной URL-путь после входа
            else:
                # Обработка ошибки аутентификации
                pass
    else:
        form = LoginForm()

    return render(request, 'login_page.html', {'form': form})



# Дальше в представление views.py добавляем utils.py
from .utils import SessionManager
session_manager = SessionManager()

def login_view(request):
    if request.method == 'POST':
        # Проверка учетных данных пользователя
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверка учетных данных и аутентификация пользователя (здесь предполагается, что есть соответствующая логика)
        if username == 'user' and password == 'password':
            # Аутентификация успешна, создаем сеанс для пользователя
            user_id = 123  # Здесь должен быть ID аутентифицированного пользователя
            session_manager.create_session(user_id)

            # После создания сеанса, можно перенаправить пользователя на главную страницу index.html
            return redirect('index')

    # Если пользователь не аутентифицирован или произошла ошибка аутентификации, возвращаем страницу входа с формой
    #return render(request, 'login.html')
    return redirect('index')

