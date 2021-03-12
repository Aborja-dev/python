from io import open
import pickle

class Link:

    # Constructor de clase
    def __init__(self, nombre, links, password):
        self.nombre = nombre
        self.links = links
        self.password = password
        self.lista()
        print('Links cargados')
    def lista(self):
    	self.links = self.links.split("\n")
    def __str__(self):
        return '{} '.format(self.links)


class Lista:

    lista = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,l):
        self.lista.append(l)
        self.guardar()

    def mostrar(self):
        if len(self.lista) == 0:
            print("Lista vacia")
            return
        for l in self.lista:
            print(l)
        return self.lista

    def cargar(self):
        fichero = open('datos.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.lista = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se ha cargado la lista")

    def guardar(self):
        fichero = open('datos.pckl', 'wb')
        pickle.dump(self.lista, fichero)
        fichero.close()
    def __len__(self):
       return len(self.lista)

