# Generated by Django 3.2.18 on 2024-02-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0010_alter_grant_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='students',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
