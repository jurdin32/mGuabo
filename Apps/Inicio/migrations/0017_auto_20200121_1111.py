# Generated by Django 2.0 on 2020-01-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0016_proyectos'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorio',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='directorio',
            name='facebook',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='directorio',
            name='inlink',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='directorio',
            name='twitter',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
