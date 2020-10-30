from tkinter import *

raiz = Tk()
raiz.title('Ejamplo check')

foto=PhotoImage(file='perfil.png')
Label(raiz,image=foto).pack()

Checkbutton(raiz,text='playa').pack()
Checkbutton(raiz,text='Montaña').pack()
Checkbutton(raiz,text='Turismo rural').pack()

raiz.mainloop()