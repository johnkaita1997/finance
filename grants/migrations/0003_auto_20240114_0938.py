# Generated by Django 3.2.18 on 2024-01-14 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0002_auto_20240114_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grant',
            old_name='posted',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='grant',
            old_name='unposted_date',
            new_name='deleted_date',
        ),
    ]
