from enum import unique
from random import choices
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя"""
    id = models.UUIDField(
        primary_key=True, 
        null=False, 
        unique=True, 
        default=uuid4
    )
    username = models.CharField(
        unique=True, 
        max_length=64, 
        verbose_name='Логин', 
        help_text='Логин пользователя', 
        blank=True
    )
    first_name = models.CharField(
        max_length=64, 
        help_text='Имя', 
        verbose_name='Имя', 
        blank=False
    )
    parent_name = models.CharField(
        max_length=64, 
        help_text='Отчество', 
        verbose_name='Отчество', 
        blank=True
    )
    surname = models.CharField(
        max_length=64, 
        help_text='Фамилия', 
        verbose_name='Фамилия', 
        blank=False
    )
    email = models.EmailField(
        unique=True, 
        help_text='E-mail', 
        verbose_name='E-mail'
    )
    birthday = models.DateField(
        help_text='Дата рождения', 
        verbose_name='Дата рождения'
    )
    is_active = models.BooleanField(
        help_text='Статус', 
        verbose_name='Статус', 
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text='Зарегистрирован', 
        verbose_name='Зарегистрирован'
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text='Последнее редактирование', 
        verbose_name='Последнее редактирование'
    )
    
    USER_ROLE = (
        ('A', 'Administrator'),
        ('M', 'Manager'),
        ('D', 'Developer'),
    )

    role = models.CharField(
        max_length=1, 
        choices=USER_ROLE, 
        blank=False, 
        help_text='Тип учетной записи'
    )

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'
        ordering = ['role']
    
    def __str__(self):
        """Return represtnting string for User"""
        return '%s %s %s' % (self.surname, self.first_name, self.parent_name)
