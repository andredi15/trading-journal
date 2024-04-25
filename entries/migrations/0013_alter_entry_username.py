# Generated by Django 4.2.7 on 2024-04-07 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0012_alter_entry_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usernames', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
