class Persona():
    def __init__(self,Nombre,edad,Lugar_residencia):
        self.Nombre = Nombre
        self.edad = edad
        self.Lugar_residencia = Lugar_residencia
    def descripcion(self):
        print('Nombre: ',self.Nombre,'\nEdad: ',self.edad,'\nLugar de residencia: ',self.Lugar_residencia)
class Empleado(Persona):
    def __init__(self,Nombre,edad,Lugar_residencia,salario,antiguedad):
        super().__init__(Nombre,edad,Lugar_residencia)
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()
        print('Salario: ',self.salario,'\nAntiguedad: ',self.antiguedad)
Manuel = Empleado('Manuel',43,'USA',1500,10)
Manuel.descripcion()
print('Es una persona: ',isinstance(Manuel,Persona))
print('Es un empleado: ',isinstance(Manuel,Empleado))
print('-----------------------------------------')
Esteban = Persona('Esteban',16,'ARG')
Esteban.descripcion()
print('Es una persona: ',isinstance(Esteban,Persona))
print('Es un empleado: ',isinstance(Esteban,Empleado))