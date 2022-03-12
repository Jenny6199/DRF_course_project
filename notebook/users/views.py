from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import User
from .serializers import UserModelSerializer


class UserLimitOffsetPagination(LimitOffsetPagination):
    """
    Класс содержит настройки LimitOfsetPagination, для дальнейшей
    реализации пагинатора в наборе представлений.
    """
    default_limit = 3

class UserSpecialViewSet(
    GenericViewSet,  
    ListModelMixin, 
    RetrieveModelMixin, 
    UpdateModelMixin
    ):
    """
    Класс серии представлений для модели User c реализацией пагинатора.
    Для настройки пагинатора используйте параметры limit= и offset=.
    Для выборки пользователей по логину доступна фильтрация в параметрах запроса.
    Класс позволяет просматривать список пользователей, отдельную запись, позволяет вносить изменения в запись.
    Удаление и создание новых пользователей запрещены.
    """
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination
    
    def get_queryset(self):
        """
        Переопределение метода для реализации возможности фильтрации
        по логину пользователя.
        """
        param = self.request.query_params.get('login', '')
        users = User.objects.all()
        if param:
            users = users.filter(username__contains=param)
        return users