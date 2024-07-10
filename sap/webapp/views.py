
from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.


# def bienvenido(request):
#     return HttpResponse("Hola mundo")

def bienvenido(request):
    # mensajes = {'msg1': 'Valor mensaje 1', 'msg2': 'Valor mensaje 2'}
    no_personas = Persona.objects.count() # numero de personas desde la BD
    # personas = Persona.objects.all() # numero de personas desde la BD
    personas = Persona.objects.order_by('id', 'nombre')  # ordena ascendentemente
    # personas = Persona.objects.order_by('-id') # ordena descendentemente

    return render(request, 'bienvenido.html',
                  {'no_personas': no_personas, 'personas': personas}) # Debe de estar siempre en el directorio de templates
# def despedirse(request):
#     return HttpResponse("despedida desde django")
