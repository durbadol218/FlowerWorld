# Generated by Django 5.1 on 2024-09-04 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_alter_flowercategory_options'),
        ('order', '0003_alter_orderitem_order'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-placed_time'], 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AddField(
            model_name='order',
            name='flower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flowers.flower'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(default=0, verbose_name='Total amount of order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Successful', 'Successful'), ('Cancelled', 'Cancelled'), ('Failed', 'Failed')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.account'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
