# Generated by Django 3.2.12 on 2022-06-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasting_track', '0003_alter_fastingsession_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastingsession',
            name='duration',
            field=models.FloatField(default=0, verbose_name='Duration'),
        ),
    ]
