# Generated by Django 2.0 on 2020-01-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0027_convocatorias_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='convocatorias',
            name='visitas',
            field=models.ImageField(default=1, upload_to=''),
        ),
    ]