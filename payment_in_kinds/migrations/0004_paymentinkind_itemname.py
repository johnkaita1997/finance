# Generated by Django 3.2.18 on 2023-12-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_in_kinds', '0003_alter_paymentinkind_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentinkind',
            name='itemName',
            field=models.CharField(blank=True, default='None', max_length=255, null=True),
        ),
    ]
