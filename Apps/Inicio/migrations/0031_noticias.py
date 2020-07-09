# Generated by Django 2.0 on 2020-01-23 14:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0030_auto_20200123_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('imagen', models.ImageField(upload_to='noticias')),
                ('descripcion_corta', models.CharField(max_length=160)),
                ('pagina', ckeditor_uploader.fields.RichTextUploadingField()),
                ('visitas', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': '5. Noticias',
            },
        ),
    ]
