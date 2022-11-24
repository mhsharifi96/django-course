from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required

# Create your views here.


def sample_view(request):
    
    token = request.GET.get('token',None)
    user = authenticate(token=token)
    print('user :::::::::::',user)
    if user is not None:
        login(request,user)
    else : 
        return HttpResponse('not found token')


    return HttpResponse(f'email {user.email}')

@login_required
def secert_view(request):
    return HttpResponse('this is secret view ')