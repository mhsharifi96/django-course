from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login


def custom_login(request):
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/#how-to-log-a-user-in
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        HttpResponse('username or password incorrect!')
        # Return an 'invalid login' error message.
        ...
    
    return HttpResponse('custom login')


def signup(request):
    if  request.user.is_authenticated:
        return redirect(reverse('blog:main-page'))
    else : 
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blog:main-page')
        else:
            form = UserCreationForm()
        
        return render(request, 'registration/signup.html', {
            'form': form
        })


@login_required
def secret_page(request):
   
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'