from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    # password = None
    email = models.EmailField(_('email address'), unique=True)
    mycustom = models.EmailField(_('cusstom fields'))
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()
    
    class Meta : 
        db_table = 'customUser'

    def __str__(self):
        return self.email