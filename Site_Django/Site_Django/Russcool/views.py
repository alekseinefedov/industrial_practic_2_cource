from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User



def index(request):
    # Ваш контекст
    context = {}
    # Отображение шаблона 'index.html'
    return render(request, 'Russcool/index.html', context)

def home(request):
    # Ваш контекст
    context = {}
    # Отображение шаблона 'home.html'
    return render(request, 'Russcool/home.html', context)


def register(request):
    if request.method == 'POST':
        # Проверка, что пользователь согласился с условиями использования
        if not request.POST.get('terms', False):
            return HttpResponse("Необходимо согласиться с условиями использования.", status=400)

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        # Убедитесь, что пароли совпадают
        if password == request.POST['password2']:
            # Хеширование пароля перед сохранением
            hashed_password = make_password(password)
            user = User(username=username, email=email, password=hashed_password)
            user.save()
            # Перенаправление на страницу входа или другую страницу
            return redirect('login_url')
        else:
            # Вернуть ошибку, если пароли не совпадают
            return render(request, 'register.html', {'error': 'Пароли не совпадают'})
    else:
        # Отображение страницы регистрации
        return render(request, 'register.html')