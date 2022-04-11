import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth import models
from .views import UserSpecialViewSet
from .models import User

class TestUserSpecialViewSet(TestCase):
    """
    Класс для тестирования контроллера модели User
    """
    pass
