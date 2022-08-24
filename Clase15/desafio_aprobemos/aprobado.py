import sys #recuerden que hay que importar system para poder recibir los argumentos

#Recibimos los argumentos y los guardamos en nota 1 y nota 2, 
#Recuerden que el argumento 0 es el nombre del script en este caso es aprobado.py
nota1 = int(sys.argv[1])
nota2 = int(sys.argv[2])

#si la nota 1 y 2 están entre 0 y 10, realizamos el algoritmo
#en caso que lo quiera ser mejor podrian agregar try, funciones y usar
#type o isdigit, ahora lo hacemos sencillo

if((nota1<=10 and nota1>=0) and (nota2<=10 and nota2>=0)):
    #si las dos notas es mayor a 7 promociona
    if(nota1>=7 and nota2>=7):
        print("Promocionado")
    #sino, si las dos notas es mayor a 4 aprueba
    elif(nota1>= 4 and nota2>=4):
        print("Aprobado, debe rendir final")
    #sino, decimos que desaprobo y aclaramos lo que tiene que recuperar
    else:
        print("Desaprobado")
        if(nota1<4):
            print("Debe recuperar el primer parcial")
        if(nota2<4):
            print("Debe recuperar el segundo parcial")
        if(nota1< 4 and nota2<4):
            print("Desaprobó ambos parciales, debe recursar")

else:
    #si las notas están mal ingresada explica como enviar los argumentos
    print("Error esta mal los argumentos")
    print("Debe ejecutarlo así, por ejemplo: python aprobado.py 7 9")

