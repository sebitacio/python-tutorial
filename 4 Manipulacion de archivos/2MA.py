from io import open 

# leer archivo
archivo_texto = open('archivo.txt','r+') # lectura y escritura

print(archivo_texto.read())
archivo_texto.seek(4) # Se ubica en la posicion 4
print(archivo_texto.read()) # Lee desde donde esta el puntero
archivo_texto.seek(0) # Se ubica en la posicion 0
print(archivo_texto.read(11)) # se detiene en la posicion 11 desde donde esta el puntero

archivo_texto.write('Texto')

archivo_texto.close()


