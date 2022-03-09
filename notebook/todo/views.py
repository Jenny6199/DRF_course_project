from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
# Для использования APIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class ProjectModelViewSet(ModelViewSet):
    """Класс представлений для модели Project"""
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    """Класс представлений для модели ToDo"""
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


class ProjectAPIVIew(APIView):
    """Класс обработки запросов к Project"""
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects,many=True)
        return Response(serializer.data)