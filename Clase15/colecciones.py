from collections import namedtuple

Pez = namedtuple("Pez", ["nombre","especie","estaque"])

pez1 = Pez("Nemo","Payaso","P")

print(pez1)
print(pez1._asdict()) #transforma el pes1 a diccionario

#--------------------------------------------------------------
print("--------------------------------------------------------------")
from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1] #cuenta la cantidad de veces hay de nros
print(Counter(l))

cosas = "casa ventana arbol casa arbol vereda"
print(Counter(cosas))

print(Counter(cosas.split())) #split es separa por espacio y toma cada elemento y lo cuenta 

#--------------------------------------------------------------
print("--------------------------------------------------------------")
