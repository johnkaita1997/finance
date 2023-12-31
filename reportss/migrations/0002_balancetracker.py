# Generated by Django 3.2.18 on 2023-12-25 16:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('reportss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceTracker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateofcreation', models.DateField(auto_now_add=True, null=True)),
                ('balanceBefore', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('amountPaid', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('balanceAfter', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('school_id', models.UUIDField(blank=True, null=True)),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
