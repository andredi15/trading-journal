# Generated by Django 4.2.7 on 2024-04-30 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_entry_close_price_entry_open_price_entry_pnl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
