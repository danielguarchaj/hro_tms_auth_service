from django.core.management.base import BaseCommand
from authentication_service.models import CustomUser


class Command(BaseCommand):
   help = "Create a default superuser"

   def handle(self, *args, **kwargs):
       if not CustomUser.objects.filter(username='admin').exists():
           CustomUser.objects.create_superuser('admin', 'admin@dev.com', '123123')
           self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
       else:
           self.stdout.write(self.style.SUCCESS("Superuser already exists"))