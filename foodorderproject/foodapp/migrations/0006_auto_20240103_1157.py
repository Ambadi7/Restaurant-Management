# Generated by Django 3.2.5 on 2024-01-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_fooditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='status',
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='description',
            field=models.TextField(),
        ),
    ]
