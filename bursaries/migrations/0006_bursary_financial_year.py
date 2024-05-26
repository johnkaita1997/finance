# Generated by Django 3.2.18 on 2024-02-05 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_years', '0002_financialyear_previous_financial_year'),
        ('bursaries', '0005_remove_bursary_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bursary',
            name='financial_year',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bursaries', to='financial_years.financialyear'),
        ),
    ]