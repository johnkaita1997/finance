# Generated by Django 3.2.18 on 2023-12-16 15:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank_accounts', '0001_initial'),
        ('payment_methods', '0002_auto_20231206_1943'),
        ('expense_categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('school_id', models.UUIDField(blank=True, null=True)),
                ('recipientType', models.CharField(blank=True, max_length=255, null=True)),
                ('member', models.CharField(blank=True, max_length=255, null=True)),
                ('referenceNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('paymentDate', models.DateField(null=True)),
                ('paymentVoucherNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('totalAmount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('deliveryNoteNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(null=True)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vouchers', to='bank_accounts.bankaccount')),
                ('expenseCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vouchers', to='expense_categories.expensecategory')),
                ('payment_Method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vouchers', to='payment_methods.paymentmethod')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
