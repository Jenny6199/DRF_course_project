from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    """Класс представлений для модели Project"""
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    """Класс представлений для модели ToDo"""
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
