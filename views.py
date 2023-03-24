from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Desde la vista de encuestas!")
def detalle(request, pregunta_id):
    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id)
def resultados(request, pregunta_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)
def votar(request, pregunta_id):
    return HttpResponse("Estas votando por la pregunta %s." % pregunta_id)
def suma(request, pregunta_id, pregunta2_id):
    print("Resultado:")
    sumar=pregunta_id+pregunta2_id
    response="Resultado:<br>La suma de ",pregunta_id," + ",pregunta2_id," = ",sumar
    return HttpResponse(response)