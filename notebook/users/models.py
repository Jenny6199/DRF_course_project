from enum import unique
from random import choices
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.forms import BooleanField, CharField, DateField, DateTimeField, EmailField, UUIDField


class User(AbstractUser):
    """Модель пользователя"""
    uuid = UUIDField(primary_key=True, default=uuid4, null=False, unique=True)
    first_name = CharField(max_length=64, help_text='Имя', verbose_name='Имя', blank=False)
    parent_name = CharField(max_length=64, help_text='Отчество', verbose_name='Отчество', blank=True)
    surname = CharField(max_length=64, help_text='Фамилия', verbose_name='Фамилия', blank=False)
    email = EmailField(unique=True, help_text='E-mail', verbose_name='E-mail')
    birthday = DateField(help_text='Дата рождения', verbose_name='Дата рождения')
    is_active = BooleanField(help_text='Статус', verbose_name='Статус')
    created_at = DateTimeField(auto_now_add=True, help_text='Зарегистрирован', verbose_name='Зарегистрирован')
    updated_at = DateTimeField(auto_now=True, help_text='Последнее редактирование', verbose_name='Последнее редактирование')
    
    USER_ROLE = (
        ('A', 'Administrator'),
        ('M', 'Manager'),
        ('D', 'Developer'),
    )

    role = CharField(max_length=1, choices=USER_ROLE, blank=False, help_text='Тип учетной записи')

    
    def __str__(self):
        """Return represtnting string for User"""
        return '%s %s %s' % (self.surname, self.first_name, self.parent_name)
