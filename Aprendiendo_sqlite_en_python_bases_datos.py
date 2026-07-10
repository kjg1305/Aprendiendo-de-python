#para tarabajar con sql lite en python se necesita importar la libreria sqlite3
import sqlite3
# CONEXION CON LA BASE DATOS 
#empezar a crear archivos o manipularlos si existen.

#crear el archivo "agenda.db" si no existe y se conecta a el 

conexion = sqlite3.connect("agenda.db")

# se crea el cursor ( el mensajero que se encarga de la comunicacion entre python y sqlite, en si traduce la query para que ambos lenguajes la entiendan)

cursor=conexion.cursor()

#2.CREACION DE UNA TABLA

#se deben usar comillas triples para poder escribir la query en varias lineas 

cursor.execute("""
                CREATE TABLE IF NOT EXITS contactos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               telefono TEXT
               )
               """)

#3 OPERACIONES CRUD (CREATE , READ , UPDATE, DELATE)

#CREATE - INSERTAR DATOS CON EL COMANDO INSERT

cursor.execute("INSERT INTO contactos (nombre,telefono) VALUES ('karen','300123')")
cursor.execute("INSERT INTO contactos (nombre,telefono) VALUES ('juan','320456')")

# PARA GUARDAR LOS CAMBIOS FISICOS 
# Se debe usar .commit()

conexion.commit()
print("!contactos creados con exito¡")

#LEER LOS DATOS DE LA BASE DE DATOS O ARCHIVO DE ESTA 

cursor.execute("SELECT * FROM contactos")

# el cursor trae los datos pero para que sean visibles en python se usa .fetchall()
#lo que devuelve una lista de tuplas 

todos_los_contactos= cursor.fetchall()

print ("\n LISTA DE CONTACTOS ")

for fila in todos_los_contactos:
    #fila[0] es el id , fila[1] es el nombre , fila[2] es el telfono
    print (f"ID:{fila[0]} | NOMBRE: {fila[1]} | TELEFONO: {fila[2]}")

#4 FINALIZACION DE UN FLUJO 
#Siempre hay que asegurase de cerrar el cursor y conexion al terminar de trabajar con la base de datos

cursor.close()
conexion.close()