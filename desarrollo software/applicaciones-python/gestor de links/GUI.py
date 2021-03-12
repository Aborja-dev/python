from tkinter import *
import funciones as func
from functools import partial
def guardar():
	l= func.Link(nombre.get(),links.get(1.0,"end"),contraseña.get())
	c = func.Lista()
	c.agregar(l)
	links.delete(1.0,"end")
	
def mostrar(link):
	mostrar = Tk()
	texto = Text(mostrar)
	texto.config(padx=15, pady=15, selectbackground="red")
	texto.pack()
	Links = link.links
	for l in Links:
		l = "{}\n".format(l)
		print(l)
		texto.insert("insert",l)
	Label(mostrar, text="Contraseña").pack()
	label = Label(mostrar,text=link.password)
	label.pack()
agregar = Tk()
nombre=StringVar()
contraseña=StringVar()

menubar = Menu()
agregar.config(menu = menubar)
filemenu = Menu(menubar)
showmenu = Menu(menubar)
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Mostrar", menu=showmenu)
for elem in range(len(func.Lista())):
	l = func.Lista().lista[elem]
	name = l.nombre
	showmenu.add_command(label=name,command=partial(mostrar,l))


filemenu.add_command(label="Salir", command=agregar.quit)


Label(agregar, text="Nombre").grid(row=0,column=0)
entry = Entry(agregar, textvariable=nombre)
entry.grid(row=0,column=1)

Label(agregar, text="Links").grid(row=1,column=0)
links = Text(agregar)
links.grid(row=2,columns=2)
links.config(width=30, height=10, 
padx=15, pady=15, selectbackground="red")

Label(agregar, text="Password").grid(row=3,column=0)
entry2 = Entry(agregar,textvariable=contraseña)
entry2.grid(row=3,column=1)
Button(agregar,text="guardar", command=guardar).grid(row=4,column=1)
	

agregar.mainloop()