# Generated by Django 3.2.18 on 2024-01-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='academic_year',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
