# Generated by Django 5.0.3 on 2024-06-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbolistas', '0008_alter_estadio_capacidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='directors',
            field=models.ManyToManyField(blank=True, to='futbolistas.director'),
        ),
        migrations.AddField(
            model_name='user',
            name='estadios',
            field=models.ManyToManyField(blank=True, to='futbolistas.estadio'),
        ),
    ]
