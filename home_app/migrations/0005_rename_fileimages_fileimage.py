# Generated by Django 5.0.3 on 2024-03-06 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_rename_files_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileImages',
            new_name='FileImage',
        ),
    ]
