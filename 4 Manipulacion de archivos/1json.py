import json
import random
# https://www.youtube.com/watch?v=9N6a-VLBa2I

f = open('inventario1.json','w')

accesoGondolas = [[15,20],
                  [15,12],
                  [12,9],
                  [9,6],
                  [6,3],
                  [7,25],
                  [16,27],
                  [27,24],
                  [25,22]]

productos = ['pechuga de pollo',
             'Pechuga de pavo',
             'Atun',
             'Salmon',
             'Carne magra',
             'Huevos',
             'Manzana',
             'Fresa',
             'Limon',
             'Mora',
             'Kiwi',
             'Pera',
             'Banano',
             'Mantequilla de mani',
             'Aceite de oliva',
             'Yogurt griego',
             'Pan integral',
             'Lechuga',
             'Brocoli',
             'Esparragos',
             'Espinaca',
             'Pimenton',
             'Coliflor',
             'Apio',
             'Pepino',
             'Cebolla',
             'Ajo',
             'Calabaza',
             'Berenjena',
             'Avena',
             'Salvado de avena',
             'Arroz integral',
             'Pasta integral',
             'Yuca',
             'Papa',
             'Frijol',
             'Lentejas',
             'Garbanzos',
             'Almendras',
             'Nueces',
             'Mani',
             'Cafe',
             'Te Verde',
             'Aromaticas']

inventario={}
for producto in productos:
    Gondola = random.randint(0,7)
    nodo = accesoGondolas[Gondola][random.randint(0,len( accesoGondolas[Gondola])-1)]
    cantidad = random.randint(0,20)
    inventario[producto]={'Gondola':Gondola,'Nodo':nodo,'Cantidad':cantidad}


json.dump(inventario,f,indent= 2)
# load json
# data = json.loads(strind) combierte str que es valido par json en python 
# data = json.load() abre archivo json en python