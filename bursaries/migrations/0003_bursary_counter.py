# Generated by Django 3.2.18 on 2024-01-20 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursaries', '0002_auto_20231230_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='bursary',
            name='counter',
            field=models.FloatField(default=None, null=True),
        ),
    ]