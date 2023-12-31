# Generated by Django 3.2.18 on 2023-12-30 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
        ('payment_methods', '0002_paymentmethod_is_cheque'),
        ('academic_year', '0001_initial'),
        ('term', '0001_initial'),
        ('bank_accounts', '0002_auto_20231230_1636'),
        ('schoolgroups', '0001_initial'),
        ('bursaries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bursary',
            name='bankAccount',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bursaries', to='bank_accounts.bankaccount'),
        ),
        migrations.AlterField(
            model_name='bursary',
            name='currency',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bursaries', to='currencies.currency'),
        ),
        migrations.AlterField(
            model_name='bursary',
            name='paymentMethod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bursaries', to='payment_methods.paymentmethod'),
        ),
        migrations.AlterField(
            model_name='bursary',
            name='schoolgroup',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bursaries', to='schoolgroups.schoolgroup'),
        ),
        migrations.AlterField(
            model_name='bursary',
            name='term',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bursaries', to='term.term'),
        ),
        migrations.AlterField(
            model_name='bursary',
            name='year',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bursaries', to='academic_year.academicyear'),
        ),
    ]
