# Generated by Django 4.2.4 on 2024-01-21 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_auto_20240103_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='c_address',
        ),
    ]
