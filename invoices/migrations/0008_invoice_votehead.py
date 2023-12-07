# Generated by Django 3.2.18 on 2023-12-07 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voteheads', '0001_initial'),
        ('invoices', '0007_uninvoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='votehead',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='voteheads.votehead'),
        ),
    ]
