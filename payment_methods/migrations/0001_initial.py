# Generated by Django 3.2.18 on 2023-12-25 07:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateofcreation', models.DateField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('is_cash', models.BooleanField(default=False, null=True)),
                ('is_bank', models.BooleanField(default=False, null=True)),
                ('school', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paymentmethods', to='school.school')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
