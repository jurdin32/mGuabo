# Generated by Django 2.0 on 2020-01-23 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0034_auto_20200123_1212'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Radio',
            new_name='Empresas',
        ),
        migrations.DeleteModel(
            name='Aguas',
        ),
        migrations.DeleteModel(
            name='Transito',
        ),
        migrations.AlterModelOptions(
            name='empresas',
            options={'verbose_name_plural': 'Empresas'},
        ),
    ]
