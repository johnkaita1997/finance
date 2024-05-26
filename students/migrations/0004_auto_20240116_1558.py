# Generated by Django 3.2.18 on 2024-01-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_date_of_admission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.AddField(
            model_name='student',
            name='groups',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
