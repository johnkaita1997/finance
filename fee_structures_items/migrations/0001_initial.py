# Generated by Django 3.2.18 on 2023-12-01 08:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voteheads', '0001_initial'),
        ('schoolgroups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeStructureItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('boardingStatus', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('school_id', models.UUIDField()),
                ('school_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee_structures_items', to='schoolgroups.schoolgroup')),
                ('votehead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee_structures_items', to='voteheads.votehead')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
