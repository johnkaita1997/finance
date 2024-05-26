# Generated by Django 3.2.18 on 2023-12-30 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
        ('account_types', '0001_initial'),
        ('bank_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='account_type', to='account_types.accounttype'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='currency', to='currencies.currency'),
        ),
    ]