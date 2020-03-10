from django.core.management.base import BaseCommand
from users.models import User


def Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(""))

