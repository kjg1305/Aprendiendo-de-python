import sqlite3
import random
import os 
#SACAR LA RUTA DE DONDE SE DEBE CREAR EL ARCHIVO DE LA BASE DE DATOS , ASI SE CREA SOLO EN LA CARPETA INDICADA
ruta_carpeta=os.path.dirname(os.path.abspath(__file__))
ruta_base_datos=os.path.join(ruta_carpeta,"parqueadero.db")

#CREAioCION DE BASE DE DATOS 
conexion= sqlite3.connect(ruta_base_datos)
cursor=conexion.cursor()
#PARA PODER USAR CLAVES FORANEAS 
cursor.execute("PRAGMA foreign_keys = ON;")
#CREACION DE LAS TABLAS DEL SISTEMA DE PARQUEADERO
#TABLA PROPIETARIO
cursor.execute("""
                CREATE TABLE IF NOT EXISTS propietario(
                ID_PROPIETARIO INTEGER PRIMARY KEY AUTOINCREMENT,
                CEDULA_PRO TEXT,
                NOMBRE TEXT,
                CELULAR TEXT,
                CORREO TEXT
               )

                """)
#TABLA VEHICULOS 
cursor.execute("""
                CREATE TABLE IF NOT EXISTS vehiculos (
                ID_VEHICULO INTEGER PRIMARY KEY AUTOINCREMENT,
                PLACA TEXT ,
                MARCA TEXT,
                COLOR TEXT 
               )
                """)
#TABLA REGUISTROS DE INGRESO Y SALIDA DE VEHICULOS RELACIOANADOS A SU PROPIETARIO
cursor.execute("""
                CREATE TABLE IF NOT EXISTS registros_parqueadero(
                ID_REGISTRO INTEGER PRIMARY KEY AUTOINCREMENT,
                ID_PROPIETARIO INTEGER,
                ID_VEHICULO INTEGER,
                FECHA_INGRESO TEXT,
                FECHA_SALIDA TEXT ,
                VALOR_PAGADO REAL,
                FOREIGN KEY (ID_PROPIETARIO) REFERENCES propietario (ID_PROPIETARIO), 
                FOREIGN KEY (ID_VEHICULO) REFERENCES vehiculos (ID_VEHICULO)
               )
                """)

#INSERCION DE DATOS EN LAS TABLAS 
#LISTAS DE DATOS PARA COMBINAR  LOS DATOS  HE INSERTAR EN LA TABLA  DE LOS PROPIETARIOS

nombres=["JUAN","MARIA","CARLOS","ANA","LUIS","DIANA","PEDRO","LAURA","ANDRES","SOFIA","LAURA","ESTEFANIA","THOMAS"]
apellidos=["GOMEZ","RODRIGUEZ","LOPEZ","PEREZ","MARTINEZ","GARCIA","SILVA","TORRES","PINZON","DIAZ","VANEGAS","GARCIA"]
dominios=["gmail.com","ooutlook.com","yahoo.com"]

#BUCLE PARA CONVINAR LOS DATOS EN LAS LISTAS Y LUEGO INSERTARLOS EN LA BASE DE DATOS
for i in range (80):
    #GENERACION AUTOMATICA DE DATOS 
    cedula=random.randint(10000000,99999999)
    nombre_completo=f"{random.choice(nombres)} {random.choice(apellidos)}"
    celular=f"318{random.randint(1000000,9999999)}"
    correo=f"{nombre_completo.lower().replace(' ', '')}{random.randint(1,99)}@{random.choice(dominios)}"

    #SQL PARA INSERTAR LOS DATOS GENERADOS A LA BASE DE DATOS
    cursor.execute("""
                    INSERT INTO propietario (CEDULA_PRO,NOMBRE,CELULAR,CORREO)
                    VALUES(?,?,?,?)
                    """, (cedula,nombre_completo,celular,correo))
    conexion.commit()

#LISTAS DE DATOS PARA COMBINAR LOS DATOS HE INSERTAR EN LA TABLA DE VEHICULOS

marcas=["TOYOTA","CHEVROLET","MAZDA","KIA","RENAULT"]
colores=["NEGRO","BLANCO","GRIS","ROJO","AZUL"]
letras_placa=["AAA","BBB","CCC","DDD","EEE"]

for i in range (80):
    placa=f"{random.choice(letras_placa)}{random.randint(100,999)}"
    marca=random.choice(marcas)
    color=random.choice(colores)

    cursor.execute("""
                    INSERT INTO vehiculos (PLACA,MARCA,COLOR)
                    VALUES(?,?,?)
                    """, (placa,marca,color))
    conexion.commit()

#PARA INSERTAR LOS DATOS EN LA TABLA DE REGISTROS ES MAS DELICADO, HAY QUE TRAER PRIMERO LOS ID DE LOS CLIENTES Y  VEHICULOS,
#YA QUE LA TABLA REGISTROS TIENE A ESTOS COMO CLAVES FORANEAS
cursor.execute("SELECT ID_PROPIETARIO FROM propietario")
lista_propietarios=[fila[0] for fila in cursor.fetchall()]
cursor.execute("SELECT ID_VEHICULO FROM vehiculos")
listas_vehiculos=[fila[0] for fila in cursor.fetchall()]
#BUCLE PARA LA INSERCION DE DATOS
for i in range (160):
    propietario_aleatorio=random.choice(lista_propietarios)
    vehiculos_aleatorios=random.choice(listas_vehiculos)
    fecha_ingreso=f"2026-07-{random.randint(10,18)}"
    fecha_salida=f"2026-07-{random.randint(10,18)}"
    valor=random.choice([5000,8000,12000,15000]) 

    cursor.execute("""
                    INSERT INTO registros_parqueadero(ID_PROPIETARIO,ID_VEHICULO,FECHA_INGRESO,FECHA_SALIDA,VALOR_PAGADO)
                    VALUES(?,?,?,?,?)
                    """, (propietario_aleatorio,vehiculos_aleatorios,fecha_ingreso,fecha_salida,valor))
    conexion.commit()

conexion.close()