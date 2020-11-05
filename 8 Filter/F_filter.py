# La funcion filter sirve para devolver los valores que cumplen una funcion

def numero_par(num):
    if num%2 == 0:
        return True

numeros=[17,24,7,39,8,51,92]

print(list(filter(lambda num: num%2==0,numeros)))

class empleado:
    def __init__(self, nombre, cargo, salario):
        
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return '{} que trabaja com {} tiene un salario de {}'.format(self.nombre,self.cargo,self.salario)

listaEmpleados=[
    empleado('juan','director',750),
    empleado('oscar','estudiante',0),
    empleado('ricardo','profesor',440),
    empleado('esteban','profesor',540)
]

salarios_altos=filter(lambda empleado: empleado.salario>500,listaEmpleados)

for empleado1 in salarios_altos:
    print(empleado1)