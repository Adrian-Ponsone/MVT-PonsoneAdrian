from datetime import datetime
from tempfile import template
from django.http import HttpResponse
from django.template import Context, Template, loader

from Personas.models import Persona


def crear_familiar(request, nombre, apellido, edad):
    
    familiar = Persona(nombre = nombre, apellido = apellido, edad = edad , fecha_de_creacion = datetime.now()) #creo el familiar
    familiar.save()      #comando para que el familiar creado quede almacenado en la base de datos
    
    
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({'familiar' : familiar})
    
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares = Persona.objects.all()             #me permite traer de la base de datos todos los elementos del modelo Persona
    
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares' : familiares})
    
    return HttpResponse(template_renderizado)