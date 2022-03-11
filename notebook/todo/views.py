from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
# Для использования APIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Для использования GenericAPIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import mixins
# Для использования ViewSets
from rest_framework import viewsets


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


class ProjectCreateAPIView(CreateAPIView):
    """Класс представления для создания объекта модели Project"""
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectListAPIView(ListAPIView):
    """Класс представления для отображения списка моделей Project"""
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectRetrieveAPIView(RetrieveAPIView):
    """Класс представления для отображения одного из объектов моделей Project"""
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    """Класс представления для редактирования одного из объектов моделей Project"""
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectDestroyAPIView(DestroyAPIView):
    """Класс представления для удаления одного из объектов моделей Project"""
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectViewSet(viewsets.ViewSet):
    """Класс набор представлений для моделей Project"""
    renderer_classes = [JSONRenderer]

    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        projects = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(projects)
        return Response(serializer.data)

class ProjectCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer]
