from django.urls import path
from . import views
from .views import register

app_name = 'Russcool'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', register, name='register_url'),
]
