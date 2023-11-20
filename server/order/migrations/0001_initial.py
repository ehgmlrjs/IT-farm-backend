# Generated by Django 4.2.7 on 2023-11-20 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('mail_number', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address_detail', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('center', models.CharField(max_length=45)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('user_id', models.IntegerField()),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
                ('photo', models.CharField(max_length=100, null=True)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
