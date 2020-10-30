from tkinter import *

raiz = Tk()

barramenu = Menu(raiz)
raiz.config(menu=barramenu)

archivoMenu=Menu(barramenu,tearoff=0)
archivoMenu.add_command(label='Abrir')
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar com')
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar')
archivoMenu.add_command(label='Salir')

edicionMenu=Menu(barramenu)
herramientasMenu=Menu(barramenu)
ayudaMenu=Menu(barramenu)

barramenu.add_cascade(label='Archivo',menu=archivoMenu)
barramenu.add_cascade(label='Edicion',menu=edicionMenu)
barramenu.add_cascade(label='Herramientas',menu=herramientasMenu)
barramenu.add_cascade(label='Ayuda',menu=ayudaMenu)

raiz.mainloop()