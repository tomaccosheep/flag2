"""flags URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'get_stuff'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index_api/', views.index_api, name='index_api'),
	path('flags/', views.get_flags, name='flags'),
	path('flags_api/', views.get_flags_api, name='flags_api'),
	path('fav_country/', views.fav_country, name='fav_country'),
]
