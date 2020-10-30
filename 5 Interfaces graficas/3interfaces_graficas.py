from tkinter import *

# con la extencion pyw no abre la consola detras
# Raiz
raiz = Tk() # Creacion de una ventana
raiz.title('Primer GUI') # Titulo de la ventana
raiz.resizable(True,True) #(bool,bool) (largo,alto) Bloquea el redimencionamiento
# raiz.iconbitmap() # Cambia al icono de que aparece en la barra
raiz.geometry("650x350") # Cambia las dimensiones de la ventana
raiz.config(bg='Red') # cambia el color del fondo de la ventana

# Primer frame
miFrame = Frame() # Crea un frame
miFrame.pack(side='right',anchor='n',fill='x',expand=True) # Empaqueta el frame
miFrame.config(bg='Blue',width='650',height='350') # define las propiedades del frame

# Mi primer label
Label(miFrame,text='Hola este es mi primer label',fg='Red',bg='Blue',font=('Comic Sans Ms',20)).place(x=100,y=200)

raiz.mainloop() # manteer ventana a la espera

