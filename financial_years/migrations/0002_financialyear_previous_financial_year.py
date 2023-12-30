# Generated by Django 3.2.18 on 2023-12-30 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_years', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialyear',
            name='previous_financial_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='financial_years.financialyear'),
        ),
    ]
