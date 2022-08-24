class Persona:

    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
    
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def setNombre(self, nombreNuevo):
        self.__nombre = nombreNuevo
        
    def setApellido(self, apellidoNuevo):
        self.__apellido = apellidoNuevo

    def hablar(self):
        print(f"La persona {self.__nombre} esta hablando")