# Generated by Django 3.2.18 on 2024-01-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteheads', '0003_alter_votehead_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votehead',
            name='vote_head_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
