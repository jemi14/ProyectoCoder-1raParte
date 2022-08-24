from datetime import date 

def calcularEdad(fechaNacimiento): 
    hoy = date.today() 
    edad = hoy.year - fechaNacimiento.year - ((hoy.month, hoy.day) < (fechaNacimiento.month, fechaNacimiento.day)) 
                                              #resta el resultado de la comparación de los meses y días

    return edad

print(calcularEdad(date(1994, 1, 3)), "años") 