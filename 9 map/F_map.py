# La funcion map sirve para aplicar una funcion a un grupo de valores


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

def calculo_comision(empleado):
    empleado.salario=empleado.salario*1.03
    return empleado

listaEmpleadosComision=map(calculo_comision,listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)

