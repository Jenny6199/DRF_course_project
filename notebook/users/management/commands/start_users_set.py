from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'create superuser and start set of users'

    def handle(self,*args, **options):
        User.objects.create_superuser(
            username='django',
            email='django@geekbrains.local',
            password='geekbrains',
        )
        User.objects.create_user(
            first_name='Maksim',
            parent_name='Sergeevich',
            surname='Sapunov',
            email='jenny6199@yandex.ru',
            birthday='1983-08-08',
            is_active=True,
            role='A',
        )