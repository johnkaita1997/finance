# Generated by Django 3.2.18 on 2023-12-30 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
        ('academic_year', '0001_initial'),
        ('streams', '0001_initial'),
        ('voteheads', '0002_votehead_ledget_folio_number_lf'),
        ('classes', '0001_initial'),
        ('students', '0001_initial'),
        ('term', '0001_initial'),
        ('schoolgroups', '0001_initial'),
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='structure_term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='term.term'),
        ),
        migrations.AlterField(
            model_name='balance',
            name='structure_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='academic_year.academicyear'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='classes',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='classes.classes'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='currencies.currency'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='students.student'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='term',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='term.term'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='votehead',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='voteheads.votehead'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='year',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoices', to='academic_year.academicyear'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='classes',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='structures', to='classes.classes'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='structures', to='schoolgroups.schoolgroup'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='stream',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='structures', to='streams.stream'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='structure_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classes.classes'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='structure_term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='term.term'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='structure_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='academic_year.academicyear'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='structures', to='students.student'),
        ),
        migrations.AlterField(
            model_name='uninvoice',
            name='structure_class',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='classes.classes'),
        ),
        migrations.AlterField(
            model_name='uninvoice',
            name='structure_stream',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='streams.stream'),
        ),
        migrations.AlterField(
            model_name='uninvoice',
            name='structure_term',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='term.term'),
        ),
        migrations.AlterField(
            model_name='uninvoice',
            name='structure_year',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='academic_year.academicyear'),
        ),
        migrations.AlterField(
            model_name='uninvoice',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='innovation_document_creator', to='students.student'),
        ),
    ]