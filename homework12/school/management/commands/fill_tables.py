from django.core.management.base import BaseCommand
from school.fill_tables import fill_tables


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = "Fill tables with logic, described at fill_tables.py."

    def handle(self, *args, **options):
        fill_tables()
        print("Tables were filled")
