# Generated by Django 3.2.18 on 2024-02-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0002_voucher_accounttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='referallNumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
