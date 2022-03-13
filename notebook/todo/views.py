# Mодели
from .models import Project, ToDo
# Сериализаторы моделей
from .serializers import ProjectModelSerializer, ToDoModelSerializer
# Использование набора представлений (ViewSets)
from rest_framework import viewsets
from rest_framework import mixins
# Постраничный вывод (Pagination)
from rest_framework.pagination import LimitOffsetPagination
# Запросы
from django.shortcuts import get_object_or_404, render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


# TODO_VIEWSET


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    """
    Класс содержит настройки LimitOfsetPagination, для дальнейшей
    реализации пагинатора в наборе представлений.
    """
    default_limit = 20


class ToDoSpecialViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin):
    """
    Класс набора представлений для модели ToDo c реализацией фильтрации и пагинатора.
    """
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_fields = ['is_active', 'project']


# PROJECT_VIEWSET


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    """
    Класс содержит настройки LimitOfsetPagination, для дальнейшей
    реализации пагинатора в наборе представлений.
    """
    default_limit = 10


class ProjectSpecialViewSet(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.DestroyModelMixin):
    """
    Класс набора представлений для модели Project с реализацией пагинатора.
    Доступны запросы POST, GET, PUT, DELETE.
    Для обращения к конкретной записи используйте запрос с конкретным id в URL.
    (например  DELETE api/projects/7/)
    Для настройки пагинатора используйте limit=, offset= в параметрах запроса.
    (например ?limit=3&offset=3, стандартное значение-10).
    Для использования фильтра введите часть названия проекта в параметрах запроса.
    (например ?project_name=разраб)
    """
    renderer_class = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_fields = ['is_active', 'members',]

    def get_queryset(self):
        """
        Переопределение метода для реализации возможности фильтрации
        по названию проекта.
        """
        param = self.request.query_params.get('project_name', '')
        projects = Project.objects.all()
        if param:
            projects = projects.filter(project_name__contains=param)
        return projects
