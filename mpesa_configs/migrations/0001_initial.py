# Generated by Django 3.2.18 on 2024-01-28 02:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mpesaconfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('school_id', models.UUIDField(blank=True, null=True)),
                ('is_saved', models.BooleanField(default=False)),
                ('shortcode', models.CharField(max_length=255)),
                ('consumer_key', models.CharField(max_length=255)),
                ('passkey', models.CharField(max_length=255)),
                ('consumer_secret', models.CharField(max_length=255)),
                ('access_token_url', models.CharField(blank=True, default='https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', max_length=255, null=True)),
                ('checkout_url', models.CharField(blank=True, default='https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest', max_length=255, null=True)),
            ],
        ),
    ]
