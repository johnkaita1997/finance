# Generated by Django 3.2.18 on 2023-12-30 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_alter_schoolimage_creator'),
        ('voucher_attachments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucherattachment',
            name='fileid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='voucher_attachments', to='file_upload.schoolimage'),
        ),
    ]
