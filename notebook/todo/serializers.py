from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer
from .models import Project, ToDo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    """Сериализатор модели Project"""
    members = StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = [
            'project_name',
            'project_URL',
            'created_at',
            'members',
            'is_active',
        ]


class ToDoModelSerializer(HyperlinkedModelSerializer):
    """Сериализатор модели ToDo"""
    # creator = StringRelatedField(many=False)
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
