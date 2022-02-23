from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Person
from .serializers import PersonModelSerialazer


class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerialazer
