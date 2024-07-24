from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="user@mail.com")
        user.set_password("123")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
