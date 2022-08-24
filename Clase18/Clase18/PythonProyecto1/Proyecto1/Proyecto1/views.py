from pipes import Template
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request): #es una petición
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):
    dia = datetime.now()

    documentoDeTexto = f"Hoy es día: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs(request, nombre):
    documentoDeTexto = f"Mi nombre es: <h1>{nombre}</h1>"
    return HttpResponse(documentoDeTexto)

#Desafio generico

def anioNaciste(request, edad):

    try:
        anio = datetime.now().year - int(edad)
        return HttpResponse(f"Mi año de nacimento es: {anio}")
    except:
        return HttpResponse("Error")

def probandoTemplate(request):
#para la ruta del html, vamos al archivo template1.html y hacemos secundario clic y copiar ruta
    miHtml = open("C:/Users/grise/Desktop/Python/Clase17/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #Tenemos que cambiar las barras invertidas

    plantilla = Template(miHtml.read())
    #no hay olvidar importar template, from django.template import Template, Context

    miHtml.close()

    miContexto = Context()
    #Para enviar y recibir inf desde modelo a la pagina

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

#------------------------- Clase 18 ------------------------------------------------
def probandoTemplateClase18(request):

    nom = "Homero"
    ape = "Simpson"

    diccionario = {"nombre": nom, "apellido": ape } #Envias al contexto

#para la ruta del html, vamos al archivo template1.html y hacemos secundario clic y copiar ruta
    miHtml = open("C:/Users/grise/Desktop/Python/Clase18/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #Tenemos que cambiar las barras invertidas

    plantilla = Template(miHtml.read())
    #no hay olvidar importar template, from django.template import Template, Context

    miHtml.close()

    miContexto = Context(diccionario)
    #Para enviar y recibir inf desde modelo a la pagina, en este caso voy a darle el nombre y apellido

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)


#---------------------------For e If en url-------------------------------
def probandoTemplateClase18_1(request):

    nom = "Homero"
    ape = "Simpson"

    listaDeNotas = [2,2,4,5,6,1]

    diccionario = {"nombre": nom, "apellido": ape, "hoy":datetime.now(), "notas":listaDeNotas} 
    #Envias al contexto, ya esta importando datatime por from datetime import datetime

#para la ruta del html, vamos al archivo template1.html y hacemos secundario clic y copiar ruta
    miHtml = open("C:/Users/grise/Desktop/Python/Clase18/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #Tenemos que cambiar las barras invertidas

    plantilla = Template(miHtml.read())
    #no hay olvidar importar template, from django.template import Template, Context

    miHtml.close()

    miContexto = Context(diccionario)
    #Para enviar y recibir inf desde modelo a la pagina, en este caso voy a darle el nombre y apellido

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

#----------------------------------------------------------
def probandoTemplateClase18_2(request):

    nom = "Homero"
    ape = "Simpson"

    listaDeNotas = [2,2,4,5,6,1]

    diccionario = {"nombre": nom, "apellido": ape, "hoy":datetime.now(), "notas":listaDeNotas} 
    #Envias al contexto, ya esta importando datatime por from datetime import datetime

    plantilla = loader.get_template('template1.html')
    #no hay olvidar importar template, from django.template import Template, Context

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)