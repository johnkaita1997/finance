# Generated by Django 3.2.18 on 2024-02-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0008_grant_overall_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grant',
            name='schoolgroup',
        ),
        migrations.AddField(
            model_name='grant',
            name='all_students',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
