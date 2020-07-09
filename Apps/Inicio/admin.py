from django.contrib import admin

# Register your models here.
from Apps.Inicio.models import *


def getItems(Objeto,nombre):
    return Objeto.__doc__.replace(nombre+"(","").replace(")","").replace(" ","").split(",")

class InstitucionAdmin(admin.ModelAdmin):
    list_display = getItems(Institucion,"Institucion")
    list_display_links = getItems(Institucion,"Institucion")
admin.site.register(Institucion,InstitucionAdmin)

class SliderPrincipalAdmin(admin.ModelAdmin):
    list_display_links = getItems(SliderPrincipal,"SliderPrincipal")
    list_display = getItems(SliderPrincipal,"SliderPrincipal")
admin.site.register(SliderPrincipal,SliderPrincipalAdmin)

class EmpresasAdmin(admin.ModelAdmin):
    list_display = getItems(Empresas,'Empresas')
    list_display_links = getItems(Empresas,'Empresas')
admin.site.register(Empresas,EmpresasAdmin)


class TurismoAdmin(admin.ModelAdmin):
    list_display = getItems(Turismo,'Turismo')
    list_display_links = getItems(Turismo,'Turismo')
admin.site.register(Turismo,TurismoAdmin)

class DirectorioAdmin(admin.ModelAdmin):
    lista = Directorio.__doc__.replace('Directorio'+"(","").replace(")","").replace(" ","").split(",")
    lista.pop(4)
    lista.pop(8)
    list_display = lista
    list_display_links = lista
admin.site.register(Directorio,DirectorioAdmin)

class ProyectosAdmin(admin.ModelAdmin):
    list_display = getItems(Proyectos,'Proyectos')
    list_display_links = getItems(Proyectos,'Proyectos')
admin.site.register(Proyectos,ProyectosAdmin)

class ZonasAdmin(admin.ModelAdmin):
    list_display = getItems(Zonas,'Zonas')
    list_display_links = getItems(Zonas,'Zonas')
admin.site.register(Zonas,ZonasAdmin)

class ConvocatoriasAdmin(admin.ModelAdmin):
    list_display_links = getItems(Convocatorias,'Convocatorias')
    list_display = getItems(Convocatorias,'Convocatorias')
admin.site.register(Convocatorias,ConvocatoriasAdmin)

class NoticiasAdmin(admin.ModelAdmin):
    list_display = getItems(Noticias,'Noticias')
    list_display_links = getItems(Noticias,'Noticias')
admin.site.register(Noticias,NoticiasAdmin)

class LotaipAdmin(admin.ModelAdmin):
    list_display_links = getItems(Lotaip,'Lotaip')
    list_display = getItems(Lotaip,'Lotaip')
admin.site.register(Lotaip,LotaipAdmin)

class RendicionCuentasAdmin(admin.ModelAdmin):
    list_display = getItems(RencionCuentas,'RencionCuentas')
    list_display_links = getItems(RencionCuentas,'RencionCuentas')
admin.site.register(RencionCuentas,RendicionCuentasAdmin)
