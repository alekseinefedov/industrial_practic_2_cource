from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import json
import bcrypt
import os


# Путь к файлу user.json
data_path = os.path.join(settings.BASE_DIR, 'data', 'user.json')

# Функция для чтения данных из файла
def read_user_data():
    with open(data_path, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Функция для записи данных в файл
def write_user_data(users):
    with open(data_path, 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=2)

# Обработчик маршрута для корневого пути
def index(request):
    return FileResponse(open(os.path.join(settings.BASE_DIR, 'public', 'index.html'), 'rb'))

# Маршрут для обработки регистрации
@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm-password')

            # Проверка совпадения паролей
            if password != confirm_password:
                return JsonResponse({'message': 'Пароли не совпадают.'}, status=400)

            users = read_user_data()

            # Проверка на уникальность пользователя
            if any(user['username'] == username or user['email'] == email for user in users):
                return JsonResponse({'message': 'Пользователь уже существует.'}, status=400)

            # Хеширование пароля
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Добавление нового пользователя
            users.append({'id': len(users) + 1, 'username': username, 'email': email, 'password': hashed_password.decode('utf-8')})

            # Сохранение обновленного списка пользователей
            write_user_data(users)

            return JsonResponse({'message': 'Пользователь успешно зарегистрирован.'})
        except Exception as e:
            return JsonResponse({'message': 'Ошибка сервера'}, status=500)
    else:
        return JsonResponse({'message': 'Неверный запрос'}, status=400)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
