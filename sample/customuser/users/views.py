from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login
from .models import CustomUser


def sample_login(request):
    user = CustomUser.objects.get(email='mohammad@gmail.com')
    login(request,user)
    return HttpResponse('loggin')


