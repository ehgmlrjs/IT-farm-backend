# Generated by Django 4.2.7 on 2023-11-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("event_id", models.AutoField(primary_key=True, serialize=False)),
                ("photo", models.CharField(default="", max_length=255)),
                ("regdate", models.DateTimeField()),
                ("enddate", models.DateTimeField()),
            ],
        ),
    ]
