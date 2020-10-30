class Coche():
    def desplazamiento(self):
        print('Me desplazo en 4 ruedas')

class Moto():
    def desplazamiento(self):
        print('Me desplazo en 2 ruedas')

class Camion():
    def desplazamiento(self):
        print('Me desplazo en 6 ruedas')

def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()

miVehiculo = Coche()
desplazamientoVehiculo(miVehiculo)