from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=40, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='страна', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
