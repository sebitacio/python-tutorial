from tkinter import *

raiz=Tk()

varOpcion=IntVar()

def imprimir():
    print(varOpcion.get())
Label(raiz,text='Genero:').pack()
Radiobutton(raiz,text='Maculino',variable=varOpcion,value=1,command=imprimir).pack()
Radiobutton(raiz,text='Femenino',variable=varOpcion,value=2,command=imprimir).pack()


raiz.mainloop()