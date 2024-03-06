# Generated by Django 5.0.3 on 2024-03-06 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_alter_type_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='images',
        ),
        migrations.CreateModel(
            name='FileImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='files/images', verbose_name='Изображение')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home_app.files')),
            ],
        ),
    ]