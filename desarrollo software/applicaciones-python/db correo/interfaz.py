from tkinter import *
from random import choice
import db

def guardar():
	contenido = texto.get(1.0, 'end')
	lista = contenido.split("\n")
	lista = lista[:3]
	db.guardar(lista)
	texto.delete(1.0, 'end')
def cargar():
	correos = db.cargar()
	if len(correos) != 0:
		texto.delete(1.0, 'end')
		for c in correos:
			contenido ="nombre:{} \ncontraseña:{}\n\n".format(c[1],c[2])
			texto.insert('insert', contenido)	
def aleatorio():
	longitud = 12
	c = ''
	letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP"
	valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	correo = "{}@gmail.com\n".format(c.join([choice(letras) for x in range(8)]))
	p = ""
	p = p.join([choice(valores) for i in range(longitud)])
	texto.delete(1.0, 'end')
	texto.insert('insert', correo)
	texto.insert('insert', p)
root = Tk()
root.resizable(0, 0)

label = Label(root,text="Gestor de cuentas de usurio")
label.grid(row=0,columns=3)
label.config(font=("Verdana",28))

frame = Frame(root,height = 350)
frame.grid(row=3, column=0, columnspan=2) 

boton1 = Button(frame,text="Guardar",command=guardar).grid(row=0,column=0)
boton2 = Button(frame,text="Cargar",command=cargar).grid(row=0,column=1)
boton3 = Button(frame,text="Generar",command=aleatorio).grid(row=0,column=2)

texto = Text(frame)
texto.grid(row=1,columns=3)
texto.config(width=50)
texto.config(bd=0, padx=6, pady=4, font=("Arial",16))
root.mainloop()