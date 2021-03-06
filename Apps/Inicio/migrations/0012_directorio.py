# Generated by Django 2.0 on 2020-01-20 18:29

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0011_auto_20200120_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('dignidad', models.CharField(choices=[('A', 'ALCALDE'), ('C', 'CONCEJAL')], max_length=50)),
                ('foto', models.ImageField(upload_to='directorio')),
                ('datos_informativos', froala_editor.fields.FroalaField()),
            ],
        ),
    ]
