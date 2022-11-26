from django.contrib.auth.models import AbstractUser,User
from django.db import models


from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    # password = None
    email = models.EmailField('email address', unique=True)
    mycustom = models.EmailField('cusstom fields')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mycustom']

    objects = CustomUserManager()


    
    class Meta : 
        db_table = 'customUser'

    def __str__(self):
        return self.email
