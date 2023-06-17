from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=30, unique=True, verbose_name="телефон")
    username = models.CharField(max_length=30, unique=True, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, verbose_name="Эмайл", blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name="рейтинг")
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    staff = models.BooleanField(default=False, verbose_name="Сотрудник")

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
