# Generated by Django 4.2.7 on 2024-01-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_entry_strategy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='comments',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
