import sys
cadena = sys.argv[1]
repeticiones = int(sys.argv[2])
for r in   range(repeticiones):
    print(f"{r}--------{cadena}")

#es lo mismo que programa 3 pero más sencillo sin validaciones