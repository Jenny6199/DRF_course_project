from curses import use_default_colors
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ToDo, Project
from users.models import User


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
        todo = ToDo.objects.create(
            project = Project.objects.get(id=1),
            creator = User.objects.get(username='django'),
            text='hello world',   
        )
        self.client.login(username='django', password='geekbrains')
        response = self.client.put(f'/api/todo/{todo.id}/', {'text': 'hi!'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo.text, 'hi!')
        