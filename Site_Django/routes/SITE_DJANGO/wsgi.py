import os
from django.core.wsgi import get_wsgi_application

# Установка переменной окружения, указывающей на файл настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SITE_DJANGO.settings')

# Получение WSGI-приложения для использования сервером
application = get_wsgi_application()