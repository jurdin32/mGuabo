# Generated by Django 2.0 on 2020-01-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0041_auto_20200123_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotaip',
            name='mes',
            field=models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], default='Enero', max_length=30),
        ),
    ]