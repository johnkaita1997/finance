# Generated by Django 3.2.18 on 2024-02-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.CharField(max_length=20),
        ),
    ]