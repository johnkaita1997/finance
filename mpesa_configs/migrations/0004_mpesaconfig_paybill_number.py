# Generated by Django 3.2.18 on 2024-01-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_configs', '0003_mpesaconfig_callback_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesaconfig',
            name='paybill_number',
            field=models.CharField(blank=True, default='0000', max_length=255, null=True),
        ),
    ]
