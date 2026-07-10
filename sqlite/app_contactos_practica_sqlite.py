#1 ORGANIZACION SQLITE CON POO 
"""
Clase Contacto -Representa un contacto.

id
nombre
telefono

Clase ContactoDAO - DAO significa:Data Access Object

Su trabajo:

Guardar contacto
Buscar contacto
Eliminar contacto
Actualizar contacto

Así separas:
Contacto -> Representa datos

ContactoDAO -> Habla con SQLite

"""
import sqlite3
import os
class Contacto :
    def __init__ (self, id,nombre, telefono, correo):
        self.id=id
        self.nombre=nombre
        self.telefono= telefono
        self.correo=correo

class ContactoDAO:

    #CONTRUCTOR DE LOS DATOS DE LA BASE DE DATOS
    def __init__ (self,archivo_db):
        self.archivo_db=archivo_db

    #CONECTAR SQLITE CON  LA BASE DE DATOS
    def conectar(self):
        #2.MANEJO DE EXCEPCIONES 
        try:
            conexion= sqlite3.connect(self.archivo_db)
            return conexion
        except sqlite3.Error as e :
            print(f"Error al conectar la base de datos: {e}")
            return None
    
    #METODO PARA PODER CREAR LA TABLA DE CONTACTOS
    def crear_tabla(self):
        #3.DISEÑO DE BASE DE DATOS - CON LOS DATOS QUE INICIALIZAMOS EN LA CLASE contacto
        conexion=self.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS contactos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            telefono TEXT,
                            correo TEXT
                            )
                            """)
            conexion.commit()
            conexion.close()
    
    #METODO PARA GUARDAR DATOS EN LA TABLA CREADA DE CONTACTOS
    def guardar_contacto (self,contacto):
        #4. USO DE PARAMETROS "?" PARA UNA SQL INJECTION Y ASI NO TENER ATAQUES DE HAKEO
        #NUNCA CONCATENAR TEXTO COMO :" VALUES ('"+contacto.nombre +"')"

        conexion= self.conectar()
        if conexion:
            try:
                cursor =conexion.cursor()
                query="INSERT INTO contactos (nombre,telefono,correo) VALUES(?,?,?)"
                cursor.execute(query,(contacto.nombre,contacto.telefono,contacto.correo))
                conexion.commit()
                print(f" CONTACTO {contacto.nombre} GURADADO CON EXITO")
            except sqlite3.Error as e :
                print(f"ERROR AL GUARDAR LOS DATOS {e}")
            
            finally:
                conexion.close()

    #5. CONSULTAS A LA BASE DE DATOS 
    #CONSULTA BASICA PARA MOSTRAR TODOS LOS DATOS
    def mostrar_todo (self):
        conexion=self.conectar()
        if conexion:
            cursor =conexion.cursor()
            cursor.execute("SELECT * FROM contactos")
            filas= cursor.fetchall()
            conexion.close()
            return filas

    #CONSULTA DE FILATRADO PARA BUSCAR POR NOMBRE DE CONTACTO
    def buscar_por_nombre (self,nombre_buscar):
        conexion=self.conectar()
        if conexion:
            cursor =conexion.cursor()
            # el signo ? previene que un hacker inyecte codigo malicioso
            query = "SELECT id, nombre,telefono FROM contactos WHERE nombre =?"
            cursor.execute(query,(nombre_buscar,))
            filas=cursor.fetchall()
            conexion.close()
            return filas
    #CONSULAT PARA LISTAR LOS DATOS Y LIMITARLOS
    def listar_ordenados_y_limitados(self):
        conexion =self.conectar()
        if conexion:
            cursor=conexion.cursor()
            #ORDENAR ALFABETICAMENTE POR NOMBRE Y SOLO TRAE LOS TRES PRIMEROS 
            query ="SELECT * FROM contactos ORDER BY nombre ASC LIMIT 3"
            cursor.execute(query)
            filas=cursor.fetchall()
            conexion.close()
            return filas 
    #QUERY  PARA ACTUALIZAR CONTACTO
    def actualizar_contacto(self,contacto):
        conexion=self.conectar()
        if conexion :
            try:
                cursor=conexion.cursor()
                query="UPDATE contactos SET nombre =? , telefono =?,correo=? WHERE id=? "
                cursor.execute(query,(contacto.nombre,contacto.telefono,contacto.correo,contacto.id))
                conexion.commit()
                print("contacto actualizado")
            except sqlite3.Error as e :
                print(f"error al actualizar el contacto")
            finally: 
                conexion.close()

    #QUERY PARA ELIMINAR UN CONTACTO
    def eliminar_contacto(self,contacto):
        conexion =self.conectar()
        if conexion:
            try:
                cursor=conexion.cursor()
                query="DELETE FROM  contactos WHERE id =?"
                cursor.execute(query,(contacto.id,))
                conexion.commit()
                print("contacto eliminado")
            except sqlite3.Error as e :
                print ("error no se pudo eliminar el contacto")
            finally:
                conexion.close()
    
#PRUEBA DE FUNCIONAMIENTO

if __name__ == "__main__":
     
     ruta_carpeta=os.path.dirname(os.path.abspath(__file__))
     
     ruta_completa_db=os.path.join(ruta_carpeta,"mi_agenda.db")

    #INICIALIZAR LA BASE DE DATOS A TRAVES DEL DAO
     agenda_dao=ContactoDAO(ruta_completa_db)
     agenda_dao.crear_tabla()

     print("INSERTANDO DATOS DE PRUEBA")
     #SE CREAN OBJETOS DE LA CLASE CONTACTO Y SE ENVIAN AL DAO
     c1=Contacto(None,"karen","3032251","k@gmail.com")
     c2=Contacto(None,"juan","320456","j@gmail.com")
     c3=Contacto(None,"carlor","315789","c@gmail.com")
     c4=Contacto(None,"Ana","311222","a @gmail.com")
     
     agenda_dao.guardar_contacto(c1)
     agenda_dao.guardar_contacto(c2)
     agenda_dao.guardar_contacto(c3)
     agenda_dao.guardar_contacto(c4)

     print("PORBANDO MOSTRAR TODO")
     todos=agenda_dao.mostrar_todo()
     for f in todos:
         print(f)
     print("PROBANDO FILATRACION DE NOMBRE ")
     resultado_buscqueda=agenda_dao.buscar_por_nombre("karen")
     print(resultado_buscqueda)

     print("PROBANDO FILTRACION ORDENACION Y LIMITACION")
     top_tres=agenda_dao.listar_ordenados_y_limitados()
     for t in top_tres:
         print(t)

     print("PROBANDO ACTUALIZAR UN CONTACTO")
     c1_modi=Contacto(1,"KAREN SILVA","999999","KS@GMAIL.COM")
     agenda_dao.actualizar_contacto(c1_modi)
     todos=agenda_dao.mostrar_todo()
     for a in todos:
         print(a) 

     print ("PROBANDO ELIMINAR UN CONTACTO")
     agenda_dao.eliminar_contacto(c1_modi)

     print("PORBANDO MOSTRAR TODO ACTUALIZADO ")
     todos=agenda_dao.mostrar_todo()
     for f in todos:
         print(f)


    
