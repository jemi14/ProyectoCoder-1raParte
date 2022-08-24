import sys

# Comprobación de seguridad, ejecutar sólo si se reciben 2 argumentos reales
if len(sys.argv) == 3: #len es cantidad de argumentos, se fija si es 3
    texto = sys.argv[1] #si es 3, guarda en texto el primer argumento
    repeticiones = int(sys.argv[2]) #guarda el segundo elemento en repeticiones, casteado como int
    for r in range(repeticiones): #hace un for hasta esa cantidad de repeticiones que enviamos por parametro
        print(texto) #muestra el texto esa cantidad de veces
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: escribir_lineas.py "Texto" 5')

#Siempre el primero argumento o sea el cero, es el nombre del programa por eso en el if len(...)=3