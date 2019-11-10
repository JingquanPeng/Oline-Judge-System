# --coding:utf-8--
"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib import admin
from project1.apps.login.views import account
from project1.apps.login.views import manageRecord, manageParking

# the distribute center for Django server to response url
# the corresponding from url to views function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.login, name='login'),
    path('login/', account.login, name='login'),
    path('register/', account.register, name='register'),
    path('findpass/', account.find_pass, name='findpass'),
    path('allRecord/', manageRecord.allRecord, name='allRecord'),
    path('addRecord/', manageRecord.addRecord, name='addRecord'),
    path('allParkingRecord/', manageParking.allParkingRecord, name='allParkingRecord'),
    path('addParkingRecord/', manageParking.addParkingRecord, name='addParkingRecord'),
]
