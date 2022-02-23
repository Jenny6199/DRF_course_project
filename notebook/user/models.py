from django.db import models
from uuid import uuid4
from django.forms import UUIDField


class Preson(models.Model):
    """
    Класс Person
    Общая, простая модель пользователя
    ----------------------------------
    uid - первичный ключ, UUID
    first_name - текст (макс.длина 64 символа)
    last_name - текст (макс.длина 64 символа)
    parent_name - текст (макс.длина 64 символа)
    birthday - дата
    email - E-mail
    was_created = дата
    is_active = Bool
    ----------------------------------
    """
    uid = models.UUIDField(primary_key=True, default= uuid4)
    first_name = models.CharField(max_length=64, help_text='Имя', verbose_name='Имя')
    last_name = models.CharField(max_length=64, help_text='Фамилия', verbose_name='Фамилия')
    parent_name = models.CharField(max_length=64, blank=True, help_text="Отчество", verbose_name='Отчество')
    birthday = models.DateField(blank=True, help_text='дата рождения', verbose_name='Дата рождения')
    email = models.EmailField(unique=True, blank=False, help_text='E-mail', verbose_name='E-mail')
    was_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(verbose_name='Активен', default=True, blank=True)
