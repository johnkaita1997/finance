# Generated by Django 3.2.18 on 2024-02-01 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_methods', '0005_rename_is_integration_default_paymentmethod_is_mpesa_default'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentmethod',
            old_name='is_mpesa_default',
            new_name='is_mpesa_integration',
        ),
    ]
