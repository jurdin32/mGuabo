# Generated by Django 2.0 on 2020-01-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0035_auto_20200123_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='nombre',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
