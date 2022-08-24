from django.shortcuts import render
from AppDesafio18.models import Familiar
from datetime import datetime
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def crear3Familias(request):

    familiar1 = Familiar(nombre = "Homero", apellido = "Simpson", fechaDeNacimiento =datetime(1988,2,15), telefono = 1234567891, email = "homerosimpson@mail.com", estaVivo = True, peso = 101.85)
    familiar2 = Familiar(nombre = "Lisa", apellido = "Simpson", fechaDeNacimiento =datetime(1997,3,16), telefono = 1234567451, email = "lisasimpson@mail.com", estaVivo = True, peso = 75.8) 
    familiar3 = Familiar(nombre = "Bartolome", apellido = "Simpson", fechaDeNacimiento =datetime(1995,4,12), telefono = 4564567891, email = "bartsimpson@mail.com", estaVivo = False, peso = 76.5)  
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    return HttpResponse("Se cargaron 3 personas") #Http NO HTTP --- y poner from django.http import HttpResponse

#---------------------------------------------------------

def mostrarFamiliares(request):

    #Trae todos los familiares de la base de datos
    listaDeFamilia = Familiar.objects.all()

    #Así lo tenias antes-- Generaba un texto con la lista de familiares
    #for f in listaDeFamilia:
        #texto = texto + f"{f.nombre}, {f.apellido}, {f.fechaDeNacimiento} \r\n" 

    #Crear la carpeta plantillas/AppDesafio18 para guardar los html
    #cambiar en settigns DIRs (en el proyecto y poner) por ejemplo: "C:/Users/grise/Desktop/Python/Clase18/Nuestro Primer MVT/Desafio18/AppDesafio18/plantillas/AppDesafio18
    #crear el html
    #importar from django.template import loader
    #Crear el diccionario con la info, cargar la plantilla con loader, generar el documento y enviarlo con http

    diccionario = {"listaDeFamilia":listaDeFamilia}  
    plantilla=loader.get_template("muestraFamilia.html")
    documento=plantilla.render(diccionario)
        
    return HttpResponse(documento)

    #return HttpResponse(texto) Así lo tenias antes

#-------------------------------------------

def inicio(request):
    return HttpResponse("Página de inicio")