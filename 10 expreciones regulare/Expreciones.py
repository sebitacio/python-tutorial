import re

cadena='Vamos a aprender expresiones regulares'
texto = re.search('aprender',cadena) # Devuelve un objeto search si lo encuentra o None si no
print(texto) 

print(texto.start()) # Indice de inicio del texto encontrado
print(texto.end()) # Indice final de donde encuentra el texto
print(texto.span()) # Tupla inicio fin

cadena = 'Vamos a aprender python, primero instala python para programar en python'
print(re.findall('python',cadena)) # Devuelve una lista con las veces que encontro la palabra

# Metacaracteres
lista_nombres=[
    'Ana Gomez',
    'Maria Martin',
    'Sandra Lopez',
    'Santiago Martin']

for elemento in lista_nombres:
    if re.findall('^Sandra',elemento): # ^ Indica que debe estar en el inicio
        print(elemento,' El elemento inicia por sandra')
    if re.findall('Martin$',elemento):
        print(elemento,' Termina por Martin') # $ Indica que debe buscar al final

lista= [
    'hombres',
    'mujeres',
    'mascotas',
    'niños',
    'niñas'
]
for elemento in lista:
    if re.findall('niñ[oa]s',elemento): # Busca si se encuentra niños o niñas en la lista
        print(elemento,' niño[oa]s')
    if re.findall('^[a-j]',elemento): # Busca al inicio elementos que empiezan con la letra a-j
        print(elemento,' inicia con letra entre a-j')               # Distingue entre mayusculas y minusculas
    if re.findall('^[^a-j]',elemento): # Muestra los elementos que no empiezan con letras entre a-j
        print(elemento,' no inicia por letra entre a-j')




