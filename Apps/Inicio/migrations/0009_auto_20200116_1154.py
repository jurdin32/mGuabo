# Generated by Django 2.0 on 2020-01-16 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0008_auto_20200116_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderprincipal',
            name='colorTexto',
        ),
        migrations.RemoveField(
            model_name='sliderprincipal',
            name='posicionHorizontal',
        ),
        migrations.RemoveField(
            model_name='sliderprincipal',
            name='posicionVertical',
        ),
        migrations.RemoveField(
            model_name='sliderprincipal',
            name='size',
        ),
        migrations.RemoveField(
            model_name='sliderprincipal',
            name='texto',
        ),
    ]