# Generated by Django 4.2.5 on 2023-09-14 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency",
            name="rate",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
