import json
from urllib import response
from django.test import TestCase
from requests import request
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth import models
from .views import UserSpecialViewSet
from .models import User

class TestUserViewSet(TestCase):
    """
    Класс для тестирования контроллера модели User
    """
    def test_get_list(self):
        """ Получение списка пользователей"""
        factory = APIRequestFactory()
        request = factory.get('api/users/')
        view = UserSpecialViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
