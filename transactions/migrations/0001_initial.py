# Generated by Django 3.2.18 on 2024-01-29 05:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0005_alter_student_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateofcreation', models.DateField(auto_now_add=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('purpose', models.CharField(blank=True, max_length=255, null=True)),
                ('checkoutid', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('school_id', models.UUIDField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('COMPLETE', 'COMPLETE'), ('CANCELLED', 'CANCELLED'), ('FAILED', 'FAILED')], default='PENDING', max_length=100, null=True)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('receiptnumber', models.CharField(blank=True, max_length=255, null=True)),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='students.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
