from tkinter import *

# con la extencion pyw no abre la consola detras
# Raiz
raiz = Tk() # Creacion de una ventana
raiz.title('Primer GUI') # Titulo de la ventana
raiz.resizable(True,True) #(bool,bool) (largo,alto) Bloquea el redimencionamiento
# raiz.iconbitmap() # Cambia al icono de que aparece en la barra
raiz.geometry("650x350") # Cambia las dimensiones de la ventana
raiz.config(bg='Red') # cambia el color del fondo de la ventana

raiz.mainloop() # manteer ventana a la espera

