class Atleta:
    #Constructor de la clase 
  def __init__(self, n, ap, a, p, t):

    #Atributos de la instancia 
    self.__nombre = n
    self.__apellido = ap
    self.__altura = a
    self.__peso = p
    self.__telefono = t
    self.__indice = p/(a**2) #estatura * estatura, a * a

    #todo deberia ser privado para hacer una correcta orientación objeto

  def getNombre(self):
    return self.__nombre

  def getApellido(self):
    return self.__apellido

  def getAltura(self):
    return self.__altura

  def getPeso(self):
    return self.__peso

  def getTelefono(self):
    return self.__telefono

  def getIndice(self):
    return self.__indice

  def setNombre(self, nombreNuevo):
    self.__nombre = nombreNuevo
  
  def setApellido(self, apellidoNuevo):
    self.__apellido = apellidoNuevo

  def setAltura(self, alturaNuevo):
    self.__altura = alturaNuevo

  def setPeso(self, pesoNuevo):
    self.__peso = pesoNuevo

  def setTelefono(self, telefonoNuevo):
    self.__telefono = telefonoNuevo

#es importante que no se haga el seteo del indice, no todas las variables se tiene que poder modificar

  def mostrarDatoImportante(self):
    print(f"{self.getNombre()}---->{self.getIndice()}")