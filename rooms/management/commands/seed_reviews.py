import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models
from reviews import models as review_models

NAME = "reviews"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help=f"How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        rooms = room_models.Room.objects.all()
        users = user_models.User.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "check_in": lambda x: random.randint(0, 5),
                "communication": lambda x: random.randint(0, 5),
                "accuracy": lambda x: random.randint(0, 5),
                "cleanliness": lambda x: random.randint(0, 5),
                "value": lambda x: random.randint(0, 5),
                "location": lambda x: random.randint(0, 5),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))

