# Generated by Django 4.0.4 on 2022-05-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0003_prescripcion_listamedicamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescripcion',
            name='comprimidos',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='dias_tratamiento',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='frecuencia_hrs',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
