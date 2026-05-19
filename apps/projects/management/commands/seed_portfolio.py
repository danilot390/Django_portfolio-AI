from django.core.management.base import BaseCommand
from django.db import transaction

from apps.projects.management.seeds.people import (
    seed_me, seed_collaborators
)
from apps.projects.management.seeds.taxonomy import (
    seed_tags, seed_technologies, seed_categories
)
from apps.projects.management.seeds.datasets import seed_datasets
from apps.projects.management.seeds.projects import seed_projects
from apps.projects.management.seeds.profiles import seed_profile
from apps.projects.management.seeds.admin import seed_admin

class Command(BaseCommand):
    help = "Master seed for the entire portfolio application database sequentially."

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.WARNING('Starting database seeding process...')
        )

        try:
            with transaction.atomic():
                
                # admin 
                seed_admin(self.stdout)
                
                # taxonomy
                seed_tags()
                seed_technologies()
                seed_categories()
                self.stdout.write('Tags, techs, categories seeding complete...')

                # datasets
                seed_datasets()
                self.stdout.write('Datasets seeding complete...')

                # people
                seed_me()
                seed_collaborators()
                self.stdout.write('People includes the host(me) seeding complete...')

                # profile
                seed_profile()
                self.stdout.write('Profile seeding complete...')

                # projects
                seed_projects()
                self.stdout.write('Projects directory seeding complete...')

            self.stdout.write(
                self.style.SUCCESS('All components successfully seeded to the DB.')
            )
        
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'\n Seeding pipeline aborted. \nError details:{e}')
            )
            raise e