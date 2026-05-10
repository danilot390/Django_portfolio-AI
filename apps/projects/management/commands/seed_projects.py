from django.core.management.base import BaseCommand

from .helpers import *


class Command(BaseCommand):
    help = 'Seed the database with initial project data'

    def handle(self, *args, **options):
        admin_user(self)
        
        first_seed(self)

        profile_seed(self)

        self.stdout.write(self.style.SUCCESS('Database seeding complete.'))

