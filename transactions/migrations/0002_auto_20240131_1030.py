# Generated by Django 3.2.18 on 2024-01-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='checkoutid',
            new_name='invoiceNumber',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='receiptnumber',
            new_name='orgAccountBalance',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='reference',
            new_name='paid_by',
        ),
        migrations.AddField(
            model_name='transaction',
            name='thirdPartyTransID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]