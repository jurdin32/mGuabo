# Generated by Django 2.0 on 2020-01-20 17:47

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0009_auto_20200116_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='radio')),
                ('pagina', froala_editor.fields.FroalaField()),
            ],
        ),
    ]