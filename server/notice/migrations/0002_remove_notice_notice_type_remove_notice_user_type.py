# Generated by Django 4.2.7 on 2023-11-20 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notice",
            name="notice_type",
        ),
        migrations.RemoveField(
            model_name="notice",
            name="user_type",
        ),
    ]
