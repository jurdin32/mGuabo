"""mGuabo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Apps.Inicio.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('',index),
    path('directorio/alcalde', alcalde),
    path('directorio', directorio),
    path('directorio/<int:id>', directorio_persona),
    path('mision-vision/', mision_vision),
    path('turismo/', turismo),
    path('turismo/zona/<int:id>', turismo_zona),
    path('convocatorias/',convocatorias),
    path('convocatorias/<int:id>/',convocatorias_una),
    path('proyecto/<int:id>/',proyectos_uno),
    path('noticias/',noticias),
    path('noticias/<int:mes>/<int:year>/',noticias_archivo),
    path('noticias_/<int:id>/<int:mes>/', noticias_una),
    path('empresa/<int:id>/',empresa),
    path('lotaip/<int:year>/',lotaip),
    path('cuentas/<int:year>/',rendicion_cuentas),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
