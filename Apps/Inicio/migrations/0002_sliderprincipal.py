# Generated by Django 2.0 on 2020-01-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(help_text='Imagen de 1600 x 571', upload_to='sliderPrincipal')),
                ('texto', models.TextField(blank=True, null=True)),
                ('posicionHorizontal', models.CharField(choices=[('', 'Izquierda'), ('800', 'Derecha'), ('400', 'Centro')], max_length=120)),
                ('posicionVertical', models.CharField(choices=[('0px', '10px'), ('100px', '100px'), ('200px', '200px'), ('200', 'Centro'), ('300px', '300px'), ('400px', '400px')], max_length=120)),
                ('colorTexto', models.CharField(default='#fff', max_length=150)),
                ('size', models.IntegerField(default=40, help_text='Tome en cuenta que es el tamaño del texto que se mostrará sobre la imagen')),
            ],
        ),
    ]
