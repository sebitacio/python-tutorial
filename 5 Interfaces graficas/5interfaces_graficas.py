from tkinter import *

# con la extencion pyw no abre la consola detras
# Raiz
raiz = Tk() # Creacion de una ventana
raiz.title('Primer GUI') # Titulo de la ventana
raiz.resizable(True,True) #(bool,bool) (largo,alto) Bloquea el redimencionamiento
# raiz.iconbitmap() # Cambia al icono de que aparece en la barra
raiz.geometry("650x350") # Cambia las dimensiones de la ventana

minombre = StringVar()
miapellido = StringVar()
midireccion = StringVar()
micontraseña = StringVar()


# Primer frame
miFrame = Frame() # Crea un frame
miFrame.pack(side='right',anchor='n',fill='x',expand=True) # Empaqueta el frame
miFrame.config(width='650',height='350') # define las propiedades del frame

# enty + label
nombreLabel=Label(miFrame,text='Nombre:')
cuadroNombre=Entry(miFrame,textvariable=minombre)

apellidoLabel=Label(miFrame,text='Apellido:')
cuadroApellido=Entry(miFrame,textvariable=miapellido)

direccionLabel=Label(miFrame,text='Direccion:')
cuadroDireccion=Entry(miFrame,textvariable=midireccion)

contraseñaLabel=Label(miFrame,text='Contraseña:')
cuadroContraseña=Entry(miFrame,textvariable=micontraseña)

nombreLabel.grid(row=0,column=0,pady=10,padx=10)
cuadroNombre.grid(row=0,column=1,pady=10,padx=10)

apellidoLabel.grid(row=1,column=0,pady=10,padx=10)
cuadroApellido.grid(row=1,column=1,pady=10,padx=10)

direccionLabel.grid(row=2,column=0,pady=10,padx=10)
cuadroDireccion.grid(row=2,column=1,pady=10,padx=10)

contraseñaLabel.grid(row=3,column=0,pady=10,padx=10)
cuadroContraseña.grid(row=3,column=1,pady=10,padx=10)

# Primer text
comentariosLabel=Label(miFrame,text='comentarios:')
comentariosLabel.grid(row=4,column=0,pady=10,padx=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=4,column=1,pady=10,padx=10)

# Scroll bar
scrolVertical = Scrollbar(miFrame,command=textoComentario.yview)
scrolVertical.grid(row=4,column=2, sticky='nsw')
textoComentario.config(yscrollcommand=scrolVertical.set)

# Primer button
def boton():
    minombre.set('Sebastian')
    miapellido.set('Rojas')
    midireccion.set('carrera 64 # 44')
    micontraseña.set('contraseña')
botonEnvio=Button(raiz,text='Enviar',command=boton)
botonEnvio.pack()
raiz.mainloop() # manteer ventana a la espera