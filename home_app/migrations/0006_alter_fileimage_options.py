# Generated by Django 5.0.3 on 2024-03-06 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_rename_fileimages_fileimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fileimage',
            options={'verbose_name': 'Изображение файла', 'verbose_name_plural': 'Изображении файла'},
        ),
    ]