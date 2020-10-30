"""
*El nombre de una variable deb em pezar con una letra o con _ nunca con un numero.
*El nombre de una variable solo puede tener caracteres alpha numericos o _.
*Los nombres de variables son sensibles a mayusculas a y A son deferentes variables.
*Las variables fuera de funciones son variables globales y pueden usarse dentro de cualquier 
 funcion.
*Las variables dentro de las funciones son variables locales y si una variable global tiene 
 el mismo nombre que una local esta no cambiara el valor de la global o viceversa.
*Para crear una variable global dentro de una funcion o cambiar el valor de una existente 
 usa global antes del nombre de la variable ejem global x
"""
# Asignar valores --------------------------------------------------------------------------
A = 9 # Asigna 9 a la variable A
A,B,C = 1,2,3 # Asigna el valores a varias variables A=1,B=2,C=3
A = B = C = 1 # Asigna el valor de 1 a A,B y C 
global x # x se vuelve una variable global asi este en una funcion
print(A) # print se usa para mostrar el valor de las variables

# 1 Tipos de variable ----------------------------------------------------------------------
# 1.1 Numericos ----------------------------------------------------------------------------
# se dividen en enteros(int), decimales(foat) y complejos(complex)
# se puede pasar de un tipo a otro usando int(),float() y complex()
# nota: no se pueden convertir complejos en otro tipo de dato numerico
# int: Son numeros positivos o negativos enteros de longitud ilimitada
A = 5
B = -2
C = 5435414231156
# float: Son numeros positivos o negativos que tengan decimales
A = 5.9
B = -25.6
C = 1.0
D = -87.7e100 # -8.7*10^100
# complex: Son escritos con una j en la parte imaginaria
A = 5j
B = 3+45j
C = -6j
# 1.2 string -------------------------------------------------------------------------------
# son cadenas de caracteres que puede estar entre " o '
# los strings son arrglos de caracteres por lo que se puede usa [i] para extraer un elemento
A = 'Hola mundo'
B = "Hola mundo"
C = """Hola
mundo"""
A[1] # retorna (o) por que es el segundo elemento(los arregolos inician en 0)
A[0:4] # [inicio:final] retorna los elementos del 0 al 3
A[-5:-1] #[inicio:final] retorna los elementos del 5 al 1 contando alreves
len(A) # retorna la longitud del string len(A) = 10
A.strip('oH') # devueeve el string sin H o o al inicio o al final la mund
A.lower() # devuelve el string en minuscula hola mundo
A.upper() # devuelve le string en mayuscula HOLA MUNDO
A.replace('Ho','Ya') # remplaza un string por otro Yala mundo
A.split(' ') # devuelve el string dividido por el especificafo ['Hola','mundo]
"Hola" in A # revisa si el string contiene al otro True
"Hola" not in A # revisa si el string no contiene al otro False
A + ' ' + B # concatena los string Hola mundo Hola mundo
txt = 'Tengo {} años'
txt.format(30) # devuelve el string con el valor en los {} tengo 30 años
txt = 'Naci el {} del mes {} del año {}'
txt.format(3,11,1996) # devuelve Naci el 3 del mes 11 del año 1996
txt = 'Naci el {1} del mes {0} del año {2}'
txt.format(3,11,1996) # devuelve Naci el 11 del mes 3 del año 1996
# parra agregar caracteres ilegales en un strin usa \
"We are the so-called \"Vikings\" from the north."
# caracteres ilegales
# \'
# \\
# \n (agrega un nueva linea)
print("Hello\nWorld!")
# \r
print("Hello\rWorld!")
# \t (Tab)
print("Hello\tWorld!")
# \r
print("Hello\rWorld!")
# \b (espacio inverso)
print("Hello \bWorld!") # HelloWorld
# \f
# \ooo (octal value)
print("\110\145\154\154\157") # Hello
# \xhh (hex value)
print("\x48\x65\x6c\x6c\x6f")
# bolean -----------------------------------------------------------------------------------
# los booleanos son datos binarios de verdadero o falso
A = True # A es un booleano (boolean)
B = False # B es un booleano (boolean)
bool(A) # retorna False si A = 0,'',[],(),{},None,False de lo contrario es True
# Sequence ---------------------------------------------------------------------------------
# listas guardan grupos de elementos de cualquier tipo
#los arreglos no se pueden igualar por que solo se estarian referenciando por lo que los 
#cambios hechos en uno afectan al otro
# list es un conjunto de datos ordenados que se pueden cambiar.  Si duplicados
A = [1,2,3,4]
B = [5,6,7]
# editar list
A[1]=45 # cambia el valor de la lista en el valor especificado
A.append(9) # agrega el valor especificado al final de la lista
A.remove(4) # remueve el elemento especificado
A.insert(4,5) # inserta el valor(5) en el inice especificado(4)
A.pop(4) # remueve el elemento en el indice especificado
del A[4] # elimina el valor en la posicion enpecificada tambien puede eliminar la lista
B.clear() # deja la lista vacia
B = A.copy() # copia la lista A en B
B = list(A) # copia la lista A en B
B = A + [5,6,7] # extiende la lista B = [1,2,3,4,5,6,7]
A.extend([5,6,7]) # extiende la lista A = [1,2,3,4,5,6,7]
# tuple es un conjunto de elementos ordenados que no se pueden cambiar. Si duplicados
A = (1,2,3,4)
# editas tuple para agregar, eliminar o editar se debe convertir en list y luego en tuple
A = list(A)
A[0] = 5
A = tuple(A)
# tuple de un elemento
B = (1,)
# eliminasr tuple
del A
# unir tuple
A = (2,3)
C = B+A # C = (1,2,3) 
# set es un conjunto no ordenado sin indices. No duplicados
A = {1,2,3,4,5,6}
# agregar y eliminar elementos
A.add(7) # agrga un elemento
A.update([8,9]) # agregar multiples elementos
A.remove(9) # si el elemento no existe saldra error
A.discard(8) # si el elemento no existe no saldra error
A.pop() # remueve el ultimo elemento
A.clear() # limpia el set
del A # Elimina el set
A = {1,2,3}
B = {4,5,6}
C = A.union(B) # C = {1,2,3,4,5,6} tanto union como update excluyen elementos repetidos
# dictionary es un conjunto no ordenado, cambiable y con indice, con llaves y valores, 
# No duplicados
A = {
    'brand':'Fors'
    'model':'mustang'
    'year':1964
    }
# Hacer una copia
B = A.copy()
B = dict(A)
# Acceder a los elementos
B = A['model'] # B = 'mustang'
B = A.get('model') # B = 'mustang'
# Cambiar valores
A['year']=2018
A.values() # devuelve todos los valores de A
A.items() # devuelve llaves y valores de A
# Agregar elementos
A.['color'] = 'red'
# Remover elementos
A.pop('model')
A.popitem() # remueve el ultimo elemento agregado
del A['brand'] # Tambien puede remover todo el diccionario
A.clear() # limpia todos los valores



