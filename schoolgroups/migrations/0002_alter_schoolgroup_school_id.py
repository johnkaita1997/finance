# Generated by Django 3.2.18 on 2023-12-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolgroups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolgroup',
            name='school_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
