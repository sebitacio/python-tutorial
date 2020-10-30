# Clase
class Coche():
    # propiedades
    # constructor estado inicial
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # En capsular la variable evita que secambie el valor fuera de la clase
        self.__enmarcha = False
    # metodos comportamiento
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if self.__enmarcha:
            chequeo = self.__Chequeo_interno()
        if self.__enmarcha and chequeo:
            return 'El coche esta en marcha'
        elif self.__enmarcha and chequeo == False:
            return 'Algo salio mal en el chequeo'
        else:
            return 'El coche esta parado'
    
    def estado(self):
        print('El coche tien ',self.__ruedas,' ruedas. Un ancho de ',self.__anchoChasis,' y un largo ',self.__largoChasis)

    def __Chequeo_interno(self): # metodo encapsulado solo se puede usar dentro de la clase
        print('realizando chequeo interno')
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'
        if self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas':
            return True
        else:
            return False

# Crear primer objeto
miCarro = Coche()
print(miCarro.arrancar(True))
miCarro.estado()

print('Segundo objeto ----------------------------------------------------------------------')
# Crear segundo objeto
miCarro2 = Coche()
print(miCarro2.arrancar(False))
miCarro2.estado()