# Generated by Django 2.0 on 2020-01-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0031_noticias'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]