from rest_framework.serializers import ModelSerializer
from .models import Project, ToDo


class ProjectModelSerializer(ModelSerializer):
    """Сериализатор модели Project"""
    class Meta:
        model = Project
        fields = [
            'project_name',
            'project_URL',
            'created_at',
            'members',
            'is_active',
        ]


class ToDoModelSerializer(ModelSerializer):
    """Сериализатор модели ToDo"""
    class Meta:
        model = ToDo
        fields = [
            'project',
            'creator',
            'short_description',
            'text',
            'created_at',
            'updated_at',
            'is_active',
        ]
