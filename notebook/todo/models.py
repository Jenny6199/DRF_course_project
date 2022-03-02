from django.db import models
from uuid import uuid4
from users.models import User

class Project(models.Model):
    """
    Модель проекта.
    ---------------------------------
    id (uuid1), 
    project_name (CharField), 
    project_URL(CharField), 
    members(ManyToManyField), 
    is_active (Boolean).
    """
    id = models.UUIDField(
        auto_created=True, 
        default=uuid4,
        verbose_name='id', 
        help_text='Идентификатор'
    )
    project_name = models.CharField(
        max_length=64, 
        blank=False,
        verbose_name='Проект', 
        help_text='Наименование проекта',
        unique=True,
    )
    project_URL = models.CharField(
        max_length=128, 
        blank=True,
        verbose_name='Репозиторий проекта', 
        help_text='Ссылка на репозиторий',
    )
    members = models.ManyToManyField(
        User, 
        null=False, 
        help_text='Пользователи учавствующие в проекте'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата начала проекта',
        help_text='Дата начала проекта',
    )
    is_active = models.BooleanField(
        default=True, 
        help_text='Статус проекта',
        )


class ToDo(models.Model):
    """
    Модель заметки.
    -----------------------------------
    id (uuid4, 
    project (ForeignKey - Project), 
    creator (one-to-one), 
    text (CharField), 
    created_at (DateTime), 
    updated_at (DateTime), 
    is_active (Boolean)
    """
    id = models.UUIDField(
        auto_created=True, 
        default=uuid4,
        verbose_name='id', 
        help_text='Идентификатор',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name='Проект',
        help_text='Заметка в составе проекта',
    )
    creator = models.OneToOneField(
        User,
        verbose_name='Владелец',
        help_text='Заметка создана пользователем:',
    )
    text = models.TextField(
        blank=False, 
        verbose_name='Текст',
        help_text='Содержание заметки',
    )
    short_description = models.CharField(
        max_length=64,
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время создания', 
        help_text='Время создания:'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,  
        help_text='Последнее редактирование'
    )
    is_active = models.BooleanField(
        default=True
    )
