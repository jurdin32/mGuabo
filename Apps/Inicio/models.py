import datetime

from ckeditor import widgets
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from froala_editor.fields import FroalaField


class Institucion(models.Model):
    nombre= models.CharField(max_length=60)
    logo = models.ImageField(upload_to="logo",null=True,blank=True)
    direccion = models.CharField(max_length=120,null=True,blank=True)
    telefono=models.CharField(max_length=60,null=True,blank=True)
    email = models.EmailField(max_length=150,null=True,blank=True)
    mision =RichTextUploadingField(null=True,blank=True)
    vision= RichTextUploadingField(null=True,blank=True)
    objetivos = RichTextUploadingField(null=True,blank=True)

    facebook=models.CharField(max_length=200,null=True,blank=True)
    twitter=models.CharField(max_length=200,null=True,blank=True)
    google_plus=models.CharField(max_length=200,null=True,blank=True)
    youtube=models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural = "1. Institución"


class SliderPrincipal(models.Model):
    imagen=models.ImageField(upload_to="sliderPrincipal",help_text="Imagen de 1600 x 571")
    estado =models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "2. Slider de Imágenes"


class Empresas(models.Model):
    nombre= models.CharField(max_length=120)
    descripcion = models.TextField()
    color_slide= ColorField(default="#ff441")
    icono =models.CharField(max_length=120, choices=(("icon-truck","icon-truck"),("icon-truck2","icon-truck2"),("icon-microphone","icon-microphone"),
                                                     ("icon-earth","icon-earth"),("icon-earth2","icon-earth2"),("icon-disk","icon-disk"),("icon-disk2","icon-disk2")))
    imagen= models.ImageField(upload_to="radio", null=True,blank=True)
    pagina = RichTextField()

    class Meta:
        verbose_name_plural = "Empresas"

class Turismo(models.Model):
    descripcion = models.TextField()
    imagen= models.ImageField(upload_to="turismo", null=True,blank=True)
    pagina = RichTextUploadingField()
    visitas = models.IntegerField(default=1)
    class Meta:
        verbose_name_plural = "Empresa de Turismo"

class Zonas(models.Model):
    descripcion = models.TextField()
    thumbail=models.ImageField(upload_to="turismo/thumbail")
    imagen = models.ImageField(upload_to="turismo", null=True, blank=True)
    pagina = RichTextUploadingField()
    visitas = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural= "Zonas y Turismo en el Cantón"


class Directorio(models.Model):
    nombre = models.CharField(max_length=120)
    dignidad = models.CharField(choices=(('A',"ALCALDE"),("C","CONCEJAL")),max_length=50)
    foto = models.ImageField(upload_to="directorio")
    mensaje_principal =RichTextUploadingField(null=True,blank=True)
    twitter = models.CharField(max_length=150,null=True,blank=True)
    facebook = models.CharField(max_length=150,null=True,blank=True)
    inlink = models.CharField(max_length=150,null=True,blank=True)
    email = models.CharField(max_length=150,null=True,blank=True)
    datos_informativos = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "3. Administración"


class Proyectos(models.Model):
    imagen = models.ImageField(upload_to='proyectos',help_text="Imagen de 585x480")
    portada =models.ImageField(upload_to='proyectos/portada',null=True,blank=True)
    titulo =models.CharField(max_length=60)
    descripcion =RichTextUploadingField()
    requisitos =RichTextUploadingField(null=True,blank=True)
    fecha_inicio = models.DateField(null=True,blank=True)
    fehca_finalizacion= models.DateField(null=True,blank=True)

    class Meta:
        verbose_name_plural="4. Futuros Proyectos"

class Convocatorias(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=120)
    imagen = models.ImageField(null=True,blank=True)
    pagina=RichTextUploadingField()
    visitas = models.IntegerField(default=1)


    class Meta:
        verbose_name_plural="Página de convocatorias"

class Noticias(models.Model):
    fecha=models.DateTimeField()
    titulo=models.CharField(max_length=200)
    banner = models.ImageField(upload_to="noticias/banner",null=True,blank=True)
    imagen =models.ImageField(upload_to='noticias', help_text="Imagen de 585 x 480")
    descripcion_corta =models.CharField(max_length=160)
    pagina = RichTextUploadingField()
    visitas =models.IntegerField(default=1)

    class Meta:
        verbose_name_plural ="5. Noticias"

class Lotaip(models.Model):
    periodo=models.IntegerField(default=2019)
    mes =models.CharField(default="Enero",choices=(
        ("Enero","Enero"),("Febrero","Febrero"),("Marzo","Marzo"),("Abril","Abril"),
        ("Mayo","Mayo"),("Junio","Junio"),("Julio","Julio"),("Agosto","Agosto"),("Septiembre","Septiembre"),
        ("Octubre","Octubre"),("Noviembre","Noviembre"),("Diciembre","Diciembre")
    ),max_length=30)
    nombre = models.CharField(max_length=120)
    descripcion=models.TextField()
    archivo=models.FileField(upload_to="lotaip")

    class Meta:
        verbose_name_plural = "6. Cumplimiento LOTAIP"

class RencionCuentas(models.Model):
    periodo=models.IntegerField(default=datetime.datetime.today().year)
    proceso= RichTextUploadingField()
    preguntas=models.FileField(upload_to="rendicionCuentas/"+str(datetime.datetime.today().year))
    acta=models.FileField(upload_to="rendicionCuentas"+str(datetime.datetime.today().year))
    invitacion=models.ImageField(upload_to="rendicionCuentas"+str(datetime.datetime.today().year))
    registro_asistencia=models.FileField(upload_to="rendicionCuentas"+str(datetime.datetime.today().year))


    class Meta:
        verbose_name_plural="7. Proceso de Rención de cuentas"