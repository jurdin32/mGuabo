# Generated by Django 2.0 on 2020-01-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0005_auto_20200116_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderprincipal',
            name='posicionHorizontal',
            field=models.CharField(blank=True, choices=[('', 'Izquierda'), ('680', 'Derecha'), ('400', 'Centro')], max_length=120, null=True),
        ),
    ]