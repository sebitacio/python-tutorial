# Estructuras
# if else else if --------------------------------------------------------------------------
A = 50
B = 30
if A<B:
    # Si la condicion se cumple haga esto
    print('A es menor que B')
elif A==B:
    # Si lo anterior no se cumple pero esta si haga esto
    print('A es igual a B')
else:
    # Si ninguna se cumple haga esto
    print('A es mayor que B')
# Si solo se tiene una opcion se puede poner todo en una linea
if A>B: print('Es mayor que B')

# Si solo se tiene una linea por opcion se puede poner en una linea
print('si es menor')if A<B else print('No se')

# Tambien se puede tenr con mas de una condicion
print('*A') if A>B else print('=') if A>=B else print('*B')

# Si se tiene un if sin accion agrega pass para evitar errore
if A>B:
    pass

# while ------------------------------------------------------------------------------------
i = 1
while i<6:
    # mientras se cumpla la condicion haga esto
    print(i)
    i+=1
else:
    #cuando la condicion no se cumpla haga esto
    print('Termine')
# si se necesita parar el loob se puede hacer asi la condicion siga siendo cierta
i=1
while i<6:
    # mientras se cumpla la condicion haga esto
    print(i)
    if i == 3:
        break
        # si la condicion se cumple pare
    i+=1
# si es necesario que pase a la siguiente iteracion se puede hacer con continue
i=1
while i<6:
    # mientras se cumpla la condicion haga esto
    i+=1
    if i == 3:
        continue
        # si la condicion se cumple pare
    print(i)
# for -------------------------------------------------------------------------------------
frutas = ['manzana','naranja','limon']
for i in frutas:
    # Para cada elemento del arrglo haga esto
    print(i)
else:
    # Cuando termine el loop haga esto
    print('termine el for')
# si se necesita parar el loob se puede hacer asi la condicion siga siendo cierta
for i in frutas:
    # Para cada elemento del arrglo haga esto
    if i == 'naranja':
        break
    print(i)
# si es necesario que pase a la siguiente iteracion se puede hacer con continue
for i in frutas:
    # Para cada elemento del arrglo haga esto
    if i == 'naranja':
        break
    print(i)
# si necesita un loop que no haga nada use pass
for i in frutas:
    # Para cada elemento del arrglo haga esto
    pass
# Funciones --------------------------------------------------------------------------------
# una funcion debe ser llamada con el mismo numero de argumentos

def funcion(nombre,apellido,pais = 'col',*dato,**datos_llaves):
    # para dar valores predefinidos a los argumentos poner = y luego el valor
    # si no sabes cuantos parametros se van a ingresar pon un * antes del nombre
    # Esto crea un tuple la cual se puede explorar
    # si no se sabe cuantos argumentos claves se va a resivir agrga ** antes del nombre
    # Esto creara un diccionario con los valores y la claves
    print('nombre'+apellido) if dato==() else print('nombre'+apellido+str(dato))
    print(datos_llaves)
    return nombre+apellido+pais
    # Si se llama la funcion haga esto

# llamar funcion
# Se puede dar el valor especifico si se conoce el nombre
funcion('sebastian',apellido='rojas',color='rojo') # llamar funcion

# lambda ----------------------------------------------------------------------------------
# Es una funcion pequeña que solo tiene una expresion
x = lambda a,b:a+b
print(x(8,3))
