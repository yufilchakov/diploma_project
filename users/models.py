from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
    
    username = None
    
    email = models.EmailField(
        unique=True, verbose_name='Почта', help_text='Укажите почту'
    )
    first_name = models.CharField(
        max_length=30, blank=True, verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=30, blank=True, verbose_name='Фамилия'
    )
    date_registration = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата регистрации'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Активен'
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
