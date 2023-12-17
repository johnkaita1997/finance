# Generated by Django 3.2.18 on 2023-12-17 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('receipts', '0008_receipt_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='classes.classes'),
        ),
    ]
