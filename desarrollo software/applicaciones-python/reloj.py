from tkinter import *
import os
from datetime import datetime

def beep():
    for x in range(3):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' %( 0.3, 400))
class Cronometer():

    def __init__(self):
        self.root = Tk()
        #Variables
        self.hora = IntVar()
        self.minuto = IntVar()
        self.segundo = IntVar()
        self.check = IntVar()
        self.inicio = 0
        self.t = 0
        self.root.geometry("260x130")
        self.root.resizable(0,0)
        Checkbutton(self.root,text="Alarma",variable=self.check,onvalue=1,offvalue=0).place(x=0,y=5)
        Button(self.root,text="Start",command=self.crono).place(x=50,y=20)
        Button(self.root,text="Stop",command=self.stop).place(x=150,y=20)
        Button(self.root,text="Reloj",command=self.watch).pack()
        self.input()
        self.root.mainloop()

        #cronometro
    def input(self):
        self.frame = Frame(self.root)
        self.frame.place(x=20,width= 210,y=50,height=50)
        self.entryH = Entry(self.frame,textvariable=self.hora,font=("Calibri 35"))
        self.entryH.place(x=0,width= 60,y=0,height=50)

        self.entryM = Entry(self.frame,textvariable=self.minuto,font=("Calibri 35"))
        self.entryM.place(x=70,width= 60,y=0,height=50) 

        self.entryS = Entry(self.frame,textvariable=self.segundo,font=("Calibri 35"))
        self.entryS.place(x=140,width= 60,y=0,height=50)
    def crono(self):
        self.inicio = self.getTime()
        self.frame.destroy()

        self.cronoLabel=Label(self.root,text="",font=("Calibri 20"),background="#ff0000")
        self.cronoLabel.place(x=20,width= 210,y=50,height=50)
        self.update()
        #entrada
            
    def update(self):
        t_object = datetime.fromtimestamp(self.inicio)
        self.cronoLabel.configure(text=t_object.strftime("%H %M %S"))
        self.cronoLabel.after(1000, self.update)
        if (self.inicio ==21600):
            self.stop()
        self.inicio = self.inicio-1
    def stop(self):
        self.cronoLabel.destroy()
        #self.beep = beep
        if self.check.get():
        	beep()
        self.input()
    def getTime(self):
        h = self.hora.get() if self.hora.get()<24 else 23
        m = self.minuto.get() if self.minuto.get()<60 else 59
        s = self.segundo.get() if self.segundo.get()<60 else 59
        self.t = (6*3600) + h*3600 + m*60 + s
        return self.t
    def watch(self):
    	self.frame.destroy()
    	x = datetime.now()
    	self.cronoLabel=Label(self.root,text=x.strftime("%H %M %S"),font=("Calibri 20"),background="#999",fg="#fff")
    	self.cronoLabel.place(x=20,width= 210,y=50,height=50)
    	self.cronoLabel.after(1000, self.watch)

Cronometer()





