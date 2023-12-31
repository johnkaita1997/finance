# Generated by Django 3.2.18 on 2023-12-25 07:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voteheads', '0001_initial'),
        ('vouchers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dateofcreation', models.DateField(auto_now_add=True, null=True)),
                ('school_id', models.UUIDField(blank=True, default=None, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('itemName', models.CharField(max_length=255)),
                ('votehead', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voucher_items', to='voteheads.votehead')),
                ('voucher', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='voucher_items', to='vouchers.voucher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
