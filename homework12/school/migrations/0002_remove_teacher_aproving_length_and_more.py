# Generated by Django 4.0 on 2022-01-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="aproving_length",
        ),
        migrations.AddField(
            model_name="teacher",
            name="approving_length",
            field=models.PositiveSmallIntegerField(
                default=5, help_text="min length of homework for approving"
            ),
        ),
    ]
