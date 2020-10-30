from io import open 

# crear archivo
archivo_texto=open('archivo.txt','w')
frase = 'Estupendo dia para estudiar Python\nel miercoles'
archivo_texto.write(frase)
archivo_texto.close()

# leer archivo
archivo_texto = open('archivo.txt','r')

lista_texto = archivo_texto.readlines() # lee el texto como una lista
# texto = archivo_texto.read() lee el texto como un string

archivo_texto.close()
print(lista_texto)

# Editar archivo
archivo_texto = open('archivo.txt','a')
archivo_texto.write('\nAhora que voy a hacer')
archivo_texto.close()