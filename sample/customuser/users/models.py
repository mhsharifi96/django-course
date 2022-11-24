from django.contrib.auth.models import AbstractUser
from django.db import models


from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    # password = None
    email = models.EmailField('email address', unique=True)
    mycustom = models.EmailField('cusstom fields')
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mycustom','email']

    objects = CustomUserManager()
    
    class Meta : 
        db_table = 'customUser'

    def __str__(self):
        return self.email