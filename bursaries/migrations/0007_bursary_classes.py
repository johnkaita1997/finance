# Generated by Django 3.2.18 on 2024-02-08 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('bursaries', '0006_bursary_financial_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='bursary',
            name='classes',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bursaries', to='classes.classes'),
        ),
    ]
