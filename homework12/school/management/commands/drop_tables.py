from django.core.management.base import BaseCommand
from school.models import Homework, HomeworkResult, Student, Teacher


class Command(BaseCommand):
    help = "Drops existing tables."

    def handle(self, *args, **options):
        Homework.objects.all().delete()
        HomeworkResult.objects.all().delete()
        Student.objects.all().delete()
        Teacher.objects.all().delete()
        print("Deleted!")
