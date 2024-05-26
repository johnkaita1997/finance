# Generated by Django 3.2.18 on 2023-12-25 07:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment_methods', '0001_initial'),
        ('financial_years', '0001_initial'),
        ('suppliers', '0001_initial'),
        ('staff', '0001_initial'),
        ('bank_accounts', '0001_initial'),
        ('expense_categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateofcreation', models.DateField(auto_now_add=True, null=True)),
                ('school_id', models.UUIDField(blank=True, null=True)),
                ('recipientType', models.CharField(blank=True, max_length=255, null=True)),
                ('other', models.CharField(blank=True, max_length=255, null=True)),
                ('referenceNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('paymentDate', models.DateField(null=True)),
                ('paymentVoucherNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=7000, null=True)),
                ('totalAmount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('deliveryNoteNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_deleted', models.DateTimeField(null=True)),
                ('counter', models.FloatField(default=None, null=True)),
                ('bank_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vouchers', to='bank_accounts.bankaccount')),
                ('expenseCategory', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vouchers', to='expense_categories.expensecategory')),
                ('financial_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vouchers', to='financial_years.financialyear')),
                ('payment_Method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vouchers', to='payment_methods.paymentmethod')),
                ('staff', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vouchers', to='staff.staff')),
                ('supplier', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vouchers', to='suppliers.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]