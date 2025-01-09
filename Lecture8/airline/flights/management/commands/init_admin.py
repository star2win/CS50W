# yourapp/management/commands/init_admin.py
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            username = os.environ['DJANGO_ADMIN_USER']
            password = os.environ['DJANGO_ADMIN_PASSWORD']
            email = os.environ['DJANGO_ADMIN_EMAIL']
        except KeyError as e:
            raise CommandError(f'Missing environment variable: {e.args[0]}')

        if not User.objects.filter(username=username).exists():
            print(f'Creating superuser {username}')
            User.objects.create_superuser(username, email, password)
        else:
            print(f'Superuser {username} already exists')