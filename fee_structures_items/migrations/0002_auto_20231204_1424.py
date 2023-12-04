# Generated by Django 3.2.18 on 2023-12-04 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolgroups', '0001_initial'),
        ('voteheads', '0001_initial'),
        ('fee_structures', '0004_remove_feestructure_fee_structure_values'),
        ('fee_structures_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feestructureitem',
            name='fee_Structure',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fee_structure_items', to='fee_structures.feestructure'),
        ),
        migrations.AlterField(
            model_name='feestructureitem',
            name='school_group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fee_structure_items', to='schoolgroups.schoolgroup'),
        ),
        migrations.AlterField(
            model_name='feestructureitem',
            name='votehead',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fee_structure_items', to='voteheads.votehead'),
        ),
    ]
