from tkinter import *
from tkinter import messagebox

raiz = Tk()
def infoAdicional():
    messagebox.showinfo("Procesador de juan",'procesador 2020')

def aviso():
    messagebox.showwarning('Licencia','profucto libre')
def abrirarchivo():
    valor = messagebox.askquestion('abrir','desea abrir un archivo')
    if valor == 'yes':
        raiz.destroy()

barramenu = Menu(raiz)

raiz.config(menu=barramenu)


archivoMenu=Menu(barramenu,tearoff=0)
archivoMenu.add_command(label='Abrir',command=abrirarchivo)
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar com')
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar',command=aviso)
archivoMenu.add_command(label='Salir',command=infoAdicional)

edicionMenu=Menu(barramenu)
herramientasMenu=Menu(barramenu)
ayudaMenu=Menu(barramenu)

barramenu.add_cascade(label='Archivo',menu=archivoMenu)
barramenu.add_cascade(label='Edicion',menu=edicionMenu)
barramenu.add_cascade(label='Herramientas',menu=herramientasMenu)
barramenu.add_cascade(label='Ayuda',menu=ayudaMenu)

raiz.mainloop()