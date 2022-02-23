from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Person


class PersonModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = 'first_name', 'parent_name', 'last_name', 'email', 'birthday', 'was_created'
