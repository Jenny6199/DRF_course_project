import json
from urllib import response
from django import views
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
    Permissions: DjangoModelPermissionsOrAnonReadOnly
    """
    def test_get_list(self):
        """ Получение списка пользователей"""
        factory = APIRequestFactory()
        request = factory.get('api/users/')
        view = UserSpecialViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_new_user(self):
        """ Попытка создания нового пользователя"""
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {
            'username': 'Testuser', 
            'email': 'tu@test.local',
            'role': 'M'
            }, format='json')
        view = UserSpecialViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {
            'userneme': 'Testuser',
            'email': 'tu@test.local',
            'birthday': '1980-01-01',
            'role': 'M',
        }, format='json')
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin_001',
            birthday='1970-01-01'
        )
        force_authenticate(request, admin)
        view = UserSpecialViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
