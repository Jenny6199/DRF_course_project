from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer
from .models import Project, ToDo
from users.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    """Сериализатор модели Project"""
    members = StringRelatedField(many=True)
    # members = UserModelSerializer
    class Meta:
        model = Project
        fields = [
            'id',
            'project_name',
            'project_URL',
            'created_at',
            'members',
            'is_active',
        ]


class ToDoModelSerializer(ModelSerializer):
    """Сериализатор модели ToDo"""
    # project = ProjectModelSerializer()
    # creator = UserModelSerializer()
    project = StringRelatedField(many=False)
    creator = StringRelatedField(many=False)
    class Meta:
        model = ToDo
        fields = [
            'id',
            'project',
            'creator',
            'short_description',
            'text',
            'created_at',
            'updated_at',
            'is_active',
        ]


class ProjectBaseSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoStartSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class ToDoBaseSerializer(ModelSerializer):
    project = ProjectBaseSerializer()
    creator = UserModelSerializer()
    class Meta:
        model = ToDo
        fields = '__all__'
