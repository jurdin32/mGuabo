from django.contrib import admin

# Register your models here.
from Apps.Repositorio.models import Imagenes, Documentos, Audios, Videos


def getItems(Objeto,nombre):
    return Objeto.__doc__.replace(nombre+"(","").replace(")","").replace(" ","").split(",")

class ImagenesAdmin(admin.ModelAdmin):
    lista = Imagenes.__doc__.replace('Imagenes'+"(","").replace(")","").replace(" ","").split(",")
    lista.append('ruta')
    lista.append('thumbail')
    list_display = lista
    list_display_links = lista
admin.site.register(Imagenes,ImagenesAdmin)

class DocumentosAdmin(admin.ModelAdmin):
    lista = Documentos.__doc__.replace('Documentos'+"(","").replace(")","").replace(" ","").split(",")
    lista.append('ruta')
    lista.append('tipo')
    list_display = lista
    list_display_links = lista
admin.site.register(Documentos,DocumentosAdmin)

class AudiosAdmin(admin.ModelAdmin):
    lista = Audios.__doc__.replace('Audios' + "(", "").replace(")", "").replace(" ", "").split(",")
    lista.append('ruta')
    list_display_links = lista
    list_display = lista
admin.site.register(Audios,AudiosAdmin)

class VideosAdmin(admin.ModelAdmin):
    lista = Videos.__doc__.replace('Videos' + "(", "").replace(")", "").replace(" ", "").split(",")
    lista.append('ruta')
    list_display_links = lista
    list_display = lista
admin.site.register(Videos,VideosAdmin)