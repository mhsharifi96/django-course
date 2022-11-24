
from django.contrib.auth import get_user_model

from django.contrib.auth.backends import BaseBackend
User = get_user_model()

class TokenBackend(BaseBackend):

    def authenticate(self,request,  token=None):
        
        try:
            user = User.objects.get(token=token)
            return user
        except User.DoesNotExist:
            pass

    def get_user(self,user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None


