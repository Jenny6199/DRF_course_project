from rest_framework.viewsets import ModelViewSet
from .models import Person
from .serializers import PersonModelSerializer


class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.filter(is_active=True)
    serializer_class = PersonModelSerializer
