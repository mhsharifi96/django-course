"""drfsample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include

from mytokenauth.views import HelloView,UserDetailAPI,RegisterUserAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ajax/', include('ajaxsample.urls')),
    path('api/', include('restsample.urls')),
    
    #token auth
    path('hello/', HelloView.as_view(), name='hello'), #new
    path("get-details/",UserDetailAPI.as_view()), #new
    path('register/',RegisterUserAPIView.as_view()), #new
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),#new
    # jwt token
    path('jwt-token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),#new
    path('jwt-token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),#new

]

