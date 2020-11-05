'''
Documentacion del modulo
'''
class areas:
    '''
    calcula areas de diferentes figuras
    '''
    def area_cuadrado(base):
        '''
        Calcula el area del cuadrado multiplicando
        base*base
        '''
        print('El area del cuadrado es '+str(base*base))
    def area2():
        '''
        ejemplo
        '''
        print(1)
def area_triangulo(base,altura):
    '''
    Calcula el area de untriangulo usando los parametros
    base y altura
    calculo: base*altura/2
    '''
    print('El area del triangulo es '+str(base*altura/2))

areas.area_cuadrado(5)

area_triangulo(6,2)

print(areas.area_cuadrado.__doc__)

help(area_triangulo)

help(areas)
