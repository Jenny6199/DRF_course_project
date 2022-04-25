from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from .models import User
from .serializers import UserModelSerializer
from django.shortcuts import get_object_or_404


class UserLimitOffsetPagination(LimitOffsetPagination):
    """
    Класс содержит настройки LimitOfsetPagination, для дальнейшей
    реализации пагинатора в наборе представлений.
    """
    default_limit = 3

class UserSpecialViewSet(
    viewsets.GenericViewSet,  
    ListModelMixin, 
    RetrieveModelMixin, 
    UpdateModelMixin
    ):
    """
    Класс серии представлений для модели User c реализацией пагинатора и фильтрации.
    Класс позволяет просматривать список пользователей, отдельную запись, позволяет вносить изменения в запись.
    Удаление и создание новых пользователей запрещены.    
    Для настройки пагинатора используйте параметры limit= и offset= (например ?limit=3&offset=3).
    Для фильтрации пользователей по должности используйте параметры запроса (например ?role=M - список менеджеров).
    Для просмотра отдельной записи пользователя добавьте UUID пользователя в URL.
    """
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination
    
    def get_queryset(self):
        """
        Переопределение метода для реализации возможности фильтрации
        по должности пользователя.
        """
        param = self.request.query_params.get('role', '')
        users = User.objects.all()
        if param:
            users = users.filter(role__contains=param)
        return users
    
    def retrieve(self, request, pk=None):
        """Метод позволяет получить доступ к записи пользователя по его UUID"""
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)
