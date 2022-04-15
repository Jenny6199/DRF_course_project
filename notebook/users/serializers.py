from rest_framework.serializers import HyperlinkedModelSerializer
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


class UserModelSerializer_v2(HyperlinkedModelSerializer):
    """ Вторая версия сериализатора для модели пользователя."""
    class Meta:
        model = User
        fields = '__all__'
