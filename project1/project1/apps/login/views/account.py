# coding:utf-8
from django.shortcuts import render, redirect, reverse
from project1.apps.login.models import User
from django.contrib import messages


# Create your views here.

# views function
# the first parameter must be 'request'
# login controller
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username.replace(" ", "") == "") or (password.replace(" ", "") == ""):
            messages.error(request, '用户名和密码不能为空！')
            return render(request, 'login.html')
        print(username, password)
        user = User.objects.filter(username=username, password=password)
        print(user)
        if user:
            print("success!")
            return redirect(reverse('allParkingRecord'))
        else:
            messages.error(request, '用户名或密码错误！')
            return render(request, 'login.html')
    return render(request, 'login.html')


# register controller
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if (username.replace(" ", "") == "") or (password1.replace(" ", "") == ""):
            messages.error(request, '用户名和密码不能为空！')
            return render(request, 'register.html')
        if (password1 != password2):
            messages.error(request, "两次输入的密码必须一致!")
            return render(request, 'register.html')
        user = User.objects.filter(username=username)
        if user:
            messages.error(request, '用户名已被注册，请重新输入!')
            return render(request, 'register.html')
        else:
            User.objects.create(username=username, password=password1)
            messages.error(request, '注册成功!')
            print("create:", username, password1)
            return redirect(reverse('login'))
    return render(request, 'register.html')


# find pass controller
def find_pass(request):
    return render(request, 'findpass.html')
