import os

from django.contrib.sites.models import Site
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Imagenes(models.Model):

    archivo =models.ImageField(upload_to='Repositorio/Imagenes')

    def ruta(self):
        current_site = Site.objects.get_current()
        return "%s/media/%s"%(current_site,self.archivo.name)

    def thumbail(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'></img>"%self.archivo.name)

    class Meta:
        verbose_name_plural="Archivos de Imágen"

class Documentos(models.Model):
    archivo = models.FileField(upload_to='Repositorio/Documentos')

    def ruta(self):
        current_site = Site.objects.get_current()
        return "%s/media/%s" % (current_site, self.archivo.name)

    def tipo(self):
        nombre_archivo, extension = os.path.splitext("%s"%self.archivo.path)
        if extension ==".docx" or extension == ".doc":
            return mark_safe("<img src='/static/archivos/docx.jpg' style='width: 30px'></img>")
        elif extension == ".pdf":
            return mark_safe("<img src='/static/archivos/pdf.svg' style='width: 20px'></img>")
        elif extension == ".xlsx" or extension ==".xls":
            return mark_safe("<img src='/static/archivos/xlsx.jpg' style='width: 30px'></img>")
        elif extension == ".pptx" or extension == ".ppt":
            return mark_safe("<img src='/static/archivos/pptx.jpg' style='width: 30px'></img>")
        return extension

    class Meta:
        verbose_name_plural="Documentos tales como pdf,xlsx,pptx,etc"


class Audios(models.Model):
    archivo = models.FileField(upload_to="Repositorio/Audios")

    def ruta(self):
        current_site = Site.objects.get_current()
        return "%s/media/%s" % (current_site, self.archivo.name)

    class Meta:
        verbose_name_plural="Archivos de Audio"


class Videos(models.Model):
    archivo = models.FileField(upload_to="Repositorio/Videos")

    def ruta(self):
        current_site = Site.objects.get_current()
        return "%s/media/%s" % (current_site, self.archivo.name)

    class Meta:
        verbose_name_plural= "Archivos de Video"