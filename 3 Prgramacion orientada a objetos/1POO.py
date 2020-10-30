'''
La programacion orientada a objetos se basa entraer el comportamiento de los objetos de la 
vida real a los programas, por lo que se le da a cada objeto unos estados, unos atributos y
unas acciones.
Clase: Es un modelo donde se redactan las caracteristicas comunes de un grupo de objetos.
Instancia: Es un objeto o ejemplar de una clase.
Modularizacion: Permite que cada elemento funcione de forma diferente y que se pueda 
reutilizar en otro codigo.
Encapsulacion: Es como si el procedimiento o trabajo interno de una clase le es inderferente
a las demas clases.
Metodos de acceso: Son las conexiones que conectan diferentes clases
'''
# Clase
class Coche():
    # propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    # metodos comportamiento
    def arrancar(self):
        self.enmarcha = True
    def estado(self):
        if(self.enmarcha):
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'
# Crear objeto
miCarro = Coche()
# acceder propiedades
print(miCarro.enmarcha)
print(miCarro.ruedas)
# acceder comportamientos
miCarro.arrancar()
print(miCarro.enmarcha)
print(miCarro.estado())