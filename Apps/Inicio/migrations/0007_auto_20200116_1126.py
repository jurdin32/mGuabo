# Generated by Django 2.0 on 2020-01-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0006_auto_20200116_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderprincipal',
            name='posicionVertical',
            field=models.CharField(choices=[('10', '10'), ('100', '100'), ('200', '200'), ('200', 'Centro'), ('300', '300'), ('400', '400')], default='10', max_length=120),
        ),
    ]
