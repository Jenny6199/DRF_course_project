from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    """Сериализатор модели пользователя"""
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'surname',
            'first_name',
            'parent_name',
            'email', 
            'birthday',
            'email', 
            'role',
        ]


class UserModelSerializer_v2(ModelSerializer):
    """ 
    Версия сериализатора для модели пользователя
    для демонстрации версионирования API.
    (Удалены некоторые поля, сериализатор наследуется от ModelSerializer)
    """
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'surname',
            'email', 
            'birthday',
            'email', 
        ]