# Generated by Django 5.1 on 2024-09-10 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0004_remove_flower_category_flower_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flower',
            name='seller',
        ),
    ]