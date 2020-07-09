import datetime

from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from Apps.Inicio.models import *


def index(request):
    institucion=Institucion.objects.first()
    contexto={
        'correo':institucion.email,
        'telefono':institucion.telefono,
        'logo': institucion.logo,
        'institucion':institucion,
        'slider':SliderPrincipal.objects.filter(estado = True),
        'administracion':Directorio.objects.get(dignidad="A"),
        'proyectos':Proyectos.objects.all(),
        'empresas':Empresas.objects.all(),
        'turismo':Turismo.objects.first(),
        'noticias':Noticias.objects.all().order_by('-fecha'),
    }
    return render(request,'home-7.html',contexto)

def alcalde(request):
    institucion=Institucion.objects.first()
    contexto={
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion': institucion,
        'directorio': Directorio.objects.get(dignidad="A"),
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request, 'alcalde.html', contexto)

def directorio(request):
    institucion = Institucion.objects.first()
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion': institucion,

        'directorio': Directorio.objects.all(),
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request,'directorio.html',contexto)

def directorio_persona(request,id):
    institucion = Institucion.objects.first()
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'directorio': Directorio.objects.get(id=id),
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'institucion':institucion,
        'proyectos': Proyectos.objects.all(),
    }
    return render(request,'elements-4.html',contexto)

def mision_vision(request):
    institucion = Institucion.objects.first()
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion':institucion,
        'mision':institucion.mision,
        'vision':institucion.vision,
        'objetivos':institucion.objetivos,
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request,'mision-vision.html',contexto)

def turismo(request):
    institucion = Institucion.objects.first()
    try:
        visitas = Turismo.objects.first()
        visitas.visitas+=1
        visitas.save()
    except:
        pass
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion':institucion,
        'turismo': Turismo.objects.first(),
        'zonas':Zonas.objects.all(),
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request, 'turismo.html', contexto)

def turismo_zona(request,id):
    institucion = Institucion.objects.first()
    try:
        visitas = Zonas.objects.get(id=id)
        visitas.visitas+=1
        visitas.save()
    except:
        pass
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion':institucion,
        'turismo': Zonas.objects.get(id=id),
        'zonas':Zonas.objects.all(),
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request, 'turismo.html', contexto)

def convocatorias(request):
    institucion = Institucion.objects.first()
    try:
        ultima = Convocatorias.objects.last()
        ultima.visitas+=1
        ultima.save()
    except:
        pass

    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'institucion':institucion,
        'logo': institucion.logo,
        'convocatoria':Convocatorias.objects.last(),
        'convocatorias':Convocatorias.objects.all().order_by('-fecha'),
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request, 'convocatoria.html',contexto)

def convocatorias_una(request,id):
    institucion = Institucion.objects.first()
    try:
        ultima = Convocatorias.objects.last()
        ultima.visitas+=1
        ultima.save()
    except:
        pass

    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'institucion':institucion,
        'logo': institucion.logo,
        'convocatoria':Convocatorias.objects.get(id=id),
        'convocatorias':Convocatorias.objects.all().order_by('-fecha'),
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request, 'convocatoria.html',contexto)

def proyectos_uno(request,id):
    institucion = Institucion.objects.first()
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion':institucion,
        'proyecto':Proyectos.objects.get(id=id),
        'noticias': Noticias.objects.all().order_by('-fecha'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request,'proyectos.html',contexto)

def listado_noticias(request,mes=None,year=None):
    lista=None
    if mes and year:
        lista=Noticias.objects.filter(fecha__month=mes, fecha__year=year).order_by('-fecha')
    else:
        lista = Noticias.objects.all().order_by('-fecha')
    paginator = Paginator(lista, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def noticias(request):
    institucion = Institucion.objects.first()
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion':institucion,
        'noticias':listado_noticias(request),
        'archivos':Noticias.objects.annotate(available=Count('fecha')).dates('fecha', 'month'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request,'noticia.html',contexto)

def noticias_archivo(request,mes,year):
    institucion = Institucion.objects.first()
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'noticias':listado_noticias(request,mes,year),
        'institucion':institucion,
        'archivos':Noticias.objects.annotate(available=Count('fecha')).dates('fecha', 'month'),
        'proyectos': Proyectos.objects.all(),
    }
    return render(request,'noticia.html',contexto)

def noticias_una(request,id,mes):
    noticias=Noticias.objects.filter(fecha__month=mes)
    nota=noticias.get(id=id)
    nota.visitas+=1
    nota.save()
    institucion = Institucion.objects.first()
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion':institucion,
        'noticia':noticias.get(id=id),
        'noticias':noticias,
        'proyectos': Proyectos.objects.all(),
    }
    return render(request,"noticas_uno.html",contexto)

def empresa(request,id):
    institucion = Institucion.objects.first()
    empresas=Empresas.objects.all()
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion': institucion,
        'noticias': Noticias.objects.all().order_by("-fecha"),
        'proyectos': Proyectos.objects.all(),
        'empresa':empresas.get(id=id),
        'empresas':empresas
    }
    return render(request,'empresas.html',contexto)

def lotaip(request, year=0):
    institucion = Institucion.objects.first()
    if year ==0:
        year=datetime.datetime.today().year
    print(year)

    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion': institucion,
        'noticias': Noticias.objects.all().order_by("-fecha"),
        'proyectos': Proyectos.objects.all(),
        'anios':Lotaip.objects.extra(select={'periodo': 'periodo'}).values('periodo').annotate(available=Count('periodo')).order_by('periodo'),
        'meses':Lotaip.objects.filter(periodo=year).extra(select={'mes': 'mes'}).values('mes').annotate(available=Count('mes')) ,
        'lotaip':Lotaip.objects.filter(periodo=year),
    }
    return render(request, 'lotaip.html', contexto)

def rendicion_cuentas(request, year=0):
    institucion = Institucion.objects.first()
    rendicion=None
    try:
        rendicion =RencionCuentas.objects.get(periodo=year)
    except:
        pass
    if year ==0:
        year=datetime.datetime.today().year
    contexto = {
        'correo': institucion.email,
        'telefono': institucion.telefono,
        'logo': institucion.logo,
        'institucion': institucion,
        'noticias': Noticias.objects.all().order_by("-fecha"),
        'proyectos': Proyectos.objects.all(),
        'anios':RencionCuentas.objects.extra(select={'periodo': 'periodo'}).values('periodo').annotate(available=Count('periodo')),
        'cuentas':rendicion,
    }
    return render(request, 'rendicionCuentas.html', contexto)