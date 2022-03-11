from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    """Сериализатор модели пользователя"""
    class Meta:
        model = User
        fields = [
            'username',
            'surname',
            'first_name',
            'parent_name',
            'email', 
            'birthday',
            'email', 
            'role',
        ]