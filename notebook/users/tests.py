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
# APIREQUESTFACTORY

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

# APICLIENT

    def test_get_detail(self):
        """ Попытка получения детальной информации о пользователе"""
        user = User.objects.create_user(
            username='testuser',
            email='test@mail.test',
            birthday='1970-01-01',
            role='M'
        )
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_edit_guest(self):
        """ Попытка редактирования профиля пользователя без авторизации"""
        user = User.objects.create_user(
        username='testuser',
        email='test@mail.test',
        birthday='1970-01-01',
        role='M'
        )
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', {
            'username': 'hello',
            'email': 'world@net.ru'
            })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_edit_admin(self):
        """Попытка редактирования профиля пользователя администратором"""
        user = User.objects.create_user(
            username='testuser',
            email='test@mail.test',
            birthday='1970-01-01',
            role='M'
        )
        client = APIClient()     
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
        client.login(username='django', password='geekbrains')
        response = client.put(f'/api/users/{user.id}/', {
            'username': 'hello',
            'email': 'world@net.ru'
            })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.username, 'hello')
        self.assertEqual(user.email, 'world@net.ru')
        client.logout()


class TestMath(APISimpleTestCase):
    """Демонстрация работы теста APISimpleTestCase"""
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)

    