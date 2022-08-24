import random

#aleatorios en un rango
print(random.randrange(20, 50))

#aleatorios en rango
print(random.randrange(20,50,7)) #multiplo de a 7 por ejemplo el 20, 27, 34 etc

#--------------------------------------------------------------
print("--------------------------------------------------------------")

lista = [1, 2, "Hola", -2, "cosas", 3]

print(random.choice(lista)) #agarra un nro cualquiera de la lista

#--------------------------------------------------------------
print("--------------------------------------------------------------")

string = "Esto es una cadena de caracteres."

print(random.choice(string))