import json
from urllib import response
from django import views
from django.test import TestCase
from requests import request
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
# from django.contrib.auth.models import User
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
        """ Попытка создания нового пользователя администратором"""
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {
            'userneme': 'testuser_2',
            'email': 'tu@test.local',
            'birthday': '1980-01-01',
            'role': 'M',
        }, format='json')
        admin = User.objects.create_superuser(
            username='django',
            first_name='Django',
            surname='Superuser',
            email='django@geekbrains.local',
            password='geekbrains',
            birthday='1970-01-01',
            is_active=True,
            role='A',
        )
        force_authenticate(request, admin)
        view = UserSpecialViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
