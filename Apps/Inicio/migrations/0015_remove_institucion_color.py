# Generated by Django 2.0 on 2020-01-20 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0014_institucion_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucion',
            name='color',
        ),
    ]