from django.shortcuts import render
from AppDesafio18.models import Familiar
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

def crear3Familias(request):

    familiar1 = Familiar(nombre = "Homero", apellido = "Simpson", fechaDeNacimiento =datetime(1988,2,15), telefono = 1234567891, email = "homerosimpson@mail.com", estaVivo = True, peso = 101.85)
    familiar2 = Familiar(nombre = "Lisa", apellido = "Simpson", fechaDeNacimiento =datetime(1997,3,16), telefono = 1234567451, email = "lisasimpson@mail.com", estaVivo = True, peso = 75.8) 
    familiar3 = Familiar(nombre = "Bartolome", apellido = "Simpson", fechaDeNacimiento =datetime(1995,4,12), telefono = 4564567891, email = "bartsimpson@mail.com", estaVivo = False, peso = 76.5)  
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    return HttpResponse("Se cargaron 3 personas") #Http NO HTTP --- y poner from django.http import HttpResponse

def mostrarFamiliares(request):

    listaDeFamilia = Familiar.objects.all()

    texto = ""

    for f in listaDeFamilia:
        texto = texto + f"{f.nombre}, {f.apellido}, {f.fechaDeNacimiento} <br>" 

    return HttpResponse(texto)

def inicio(request):
    return HttpResponse("Página de inicio")