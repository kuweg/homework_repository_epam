from django.core.management.base import BaseCommand
from school.fill_tables import fill_tables


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = "our help string comes here"

    def handle(self, *args, **options):
        fill_tables()
        print("Tables were filled")
