# Generated by Django 3.2.18 on 2024-02-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursaries', '0003_bursary_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='bursary',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True),
        ),
    ]