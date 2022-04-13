from curses import use_default_colors
import json
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ToDo, Project
from users.models import User
from mixer.backend.django import mixer



class TestToDoViewSet(APITestCase):
    def test_ToDoViewSet_get_list(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_ToDoViewSet_edit_ToDo_by_admin(self):
        """ Попытка редактирования заметки администратором"""
        project = Project.objects.create(
            project_name='Тестовый проект',
            project_URL='45.129.14.61',
            is_active=True,
        )    
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
        todo = mixer.blend(ToDo)
        self.client.login(username='django', password='geekbrains')
        response = self.client.put(f'/api/todo/{todo.id}/', {'text': 'hi!'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo.text, 'hi!')

    def test_ToDoViewSet_get_detail(self):
        """ Попытка получения данных заметки"""
        todo = mixer.blend(ToDo, text='Изучение DRF')
        response = self.client.get('f/api/todo/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_todo = json.loads(response.content)
        self.assertEqual(response_todo['text'], 'Изучение DRF')
        
        