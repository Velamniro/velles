# Generated by Django 5.0.3 on 2024-03-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0011_game_slug_type_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='type',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
    ]