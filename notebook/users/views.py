from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    """Класс серии представлений для модели User"""
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

