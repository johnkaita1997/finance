# Generated by Django 3.2.18 on 2023-12-30 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
        ('academic_year', '0001_initial'),
        ('classes', '0001_initial'),
        ('students', '0001_initial'),
        ('account_types', '0001_initial'),
        ('financial_years', '0002_financialyear_previous_financial_year'),
        ('term', '0001_initial'),
        ('bank_accounts', '0002_auto_20231230_1636'),
        ('payment_methods', '0003_alter_paymentmethod_school'),
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='account_types.accounttype'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='bank_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='bank_accounts.bankaccount'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='currencies.currency'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='financial_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='financial_years.financialyear'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='payment_method',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='payment_methods.paymentmethod'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='students.student'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='classes.classes'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='term',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='term.term'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='academic_year.academicyear'),
        ),
    ]
