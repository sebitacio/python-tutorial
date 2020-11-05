# Sirve para añadir funciones a una funcion

'''
des funcion_decorador(funcion):
    def funcion_interna():
        # codigo
    return funcion_interna
'''

# Decorador inutil

def decorador(funcion):
    
    def interna():
        print('Se va a hacer un calculo')
        funcion()
        print('Se termino el calculo')
    return interna

@decorador
def suma():
    print(15+20)

@decorador
def resta():
    print(30-10)

suma()
resta()
print('-'*30)

# decorador con parametros ---------------------------------------------------
def decorador2(funcion):
    
    def interna(*args,**kwargs):
        print('Se va a hacer un calculo')
        funcion(*args,**kwargs)
        print('Se termino el calculo')
    return interna

@decorador2
def suma_p(num1,num2,num3):
    print(num1+num2+num3)

@decorador2
def resta_p(num1,num2):
    print(num1-num2)

suma_p(1,2,num3=3)
resta_p(1,2)
print('-'*30)

