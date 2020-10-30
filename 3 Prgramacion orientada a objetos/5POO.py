# Clase padre o super clase
class Vehiculos():

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self, parameter_list):
        self.frena = True
    
    def estado(self):
        print('Marca: ',self.marca,'\nModelo: ',self.modelo,'\nEn marcha: ',self.enmarcha,'\nAcelerando: ',self.acelera,'\nFrenando: ',self.frena)

#Sub clase1
class Moto(Vehiculos):
    pique = ''
    def Hpique(self):
        self.pique='Estoy haiendo un pique'
    # El metodo estado de la subclase sobre escribe el de la superclase
    def estado(self):
         print('Marca: ',self.marca,'\nModelo: ',self.modelo,'\nEn marcha: ',self.enmarcha,'\nAcelerando: ',self.acelera,'\nFrenando: ',self.frena,'\n',self.pique)

#Sub clase2
class Furgoneta(Vehiculos):
    def Carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no esta cargada'

#Clase2
class VElectricos():
    def __init__(self):
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando = True

#Sub clase3 con herencia multiple. se le da preferencia al constructor de la superclase mas a la izquierda
class BicicletaElectrica(Vehiculos,VElectricos):
    pass

# Objeto 1
miMoto = Moto('Honda','CBR')
miMoto.Hpique()
miMoto.estado()
print('--------------------------------------------------')
#objeto 2
miFurgoneta = Furgoneta('Renault','Kangoo')
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.Carga(True))
print('--------------------------------------------------')
miBici = BicicletaElectrica('Orvea','HT1030')
miBici.cargarEnergia()
print(miBici.cargando)
miBici.estado()