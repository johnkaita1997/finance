# Generated by Django 3.2.18 on 2024-02-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0002_auto_20240129_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votehead_id', models.UUIDField()),
                ('expenditure_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('income_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
