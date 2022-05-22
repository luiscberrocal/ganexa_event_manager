# Generated by Django 3.2.12 on 2022-05-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasting_track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastingsession',
            name='duration',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='fastingsession',
            name='target_duration',
            field=models.PositiveSmallIntegerField(default=16, verbose_name='Target duration'),
        ),
    ]