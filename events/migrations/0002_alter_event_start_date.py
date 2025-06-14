# Generated by Django 5.2.1 on 2025-05-28 20:32

import events.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateField(
                validators=[events.validators.validate_future_date],
                verbose_name="date started",
            ),
        ),
    ]
