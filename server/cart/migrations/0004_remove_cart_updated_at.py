# Generated by Django 4.2.7 on 2023-11-20 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0003_alter_cart_product_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="updated_at",
        ),
    ]
