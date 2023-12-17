# Generated by Django 3.2.18 on 2023-12-13 07:40

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bursaries', '0001_initial'),
        ('students', '0005_student_current_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('school_id', models.UUIDField(blank=True, default=None, null=True)),
                ('bursary', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bursaries.bursary')),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='students.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
