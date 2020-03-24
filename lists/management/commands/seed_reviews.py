import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"

class Command(BaseCommand):

    help = f"This command creats {name}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"How many {NAME} you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Romom.objects.all()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users)
            }
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        #for

        self.stdout.write(self.style.SUCCESS(f"{number}{NAME} created!"))
