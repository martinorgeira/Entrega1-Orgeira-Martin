from queue import Empty
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from home.models import Persona

def familiares(request):
    return HttpResponse("familiares")

def fecha(request):
    fechas = datetime.now()
    return HttpResponse(f"la hora y fecha es {fechas}")

def fechanacimiento(request, edad):
    fechas = datetime.now().year - edad
    return HttpResponse(f"tu fecha de nacimiento es{edad}seria{fechas}" )

def mi_template(request):
    
    cargar_archivo = open(r'E:\visuaoproyectos\orgeiraMVT\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
        
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
        
    return HttpResponse(template_renderizado)

def crear_persona(request, nombre, apellido):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona.save()
    
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'persona': persona})
    
    return HttpResponse(template_renderizado)    