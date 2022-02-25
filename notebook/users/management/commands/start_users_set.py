from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'create superuser and start set of users'

    def handle(self,*args, **options):
        User.objects.create_superuser(
            username='django',
            first_name='Django',
            surname='Superuser',
            email='django@geekbrains.local',
            password='geekbrains',
            birthday='1970-01-01',
            is_active=True,
            role='A',
        )
        User.objects.create_user(
            username='Ivanov_II',
            first_name='Иван',
            parent_name='Иванович',
            surname='Иванов',
            email='Ivan_Ivanov@example.local',
            birthday='1987-01-01',
            is_active=True,
            role='M',
        )
