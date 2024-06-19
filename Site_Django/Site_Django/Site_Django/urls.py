"""
URL configuration for Site_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Russcool.views import index, register
from Russcool import views



app_name = 'Russcool'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Russcool/', include('Russcool.urls')),
    path('register/', include('Russcool.urls')),
    path('', include('Russcool.urls')),
    path('Russcool/', index),
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('', include('Russcool.urls')),
]
