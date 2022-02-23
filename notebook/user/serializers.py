from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Person


class PersonModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
