#  Para evitar que el programa detenga la ejecucion de todas las lineas podemos
# usar la sentencia try

try:
    # Intente hacer esto
    print(5/0) # la divsion por sero es un error
except ZeroDivisionError as DivisionPorZero:
    # Si no pudo hacerlo haga esto
    print('No se puede dividir por zero')
print('se termino la ejecucion')

# Podemos tambien crear nuestras propias excepciones
if -1<0:
    raise TypeError ('No se pueden numeros negativos')
print('El programa sigue')