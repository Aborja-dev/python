import sqlite3


def crearTabla():
	conexion = sqlite3.connect('correo.db')
	cursor = conexion.cursor()
	
	cursor.execute('''CREATE TABLE IF NOT EXISTS correos (
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						direccion VARCHAR(100) UNIQUE, 
						contraseña VARCHAR(100) UNIQUE,
						descripcion VARCHAR(100)
					)''')

	conexion.commit()
	
	conexion.close()
def guardar(lista):
	conexion = sqlite3.connect('correo.db')
	cursor = conexion.cursor()
	correos = [lista]
	cursor.executemany("INSERT INTO correos VALUES (null,?,?,?)",correos)
	conexion.commit()
	conexion.close()
def cargar():
	conexion = sqlite3.connect('correo.db')
	cursor = conexion.cursor()
	cursor.execute("SELECT * FROM correos")
	correos = cursor.fetchall()
	conexion.commit()
	conexion.close()
	return correos
