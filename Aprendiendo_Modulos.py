#MODULOS

"""
¿QUE ES UN MODULO? -Simplemente un archivo.py

Exisiten por que al haber proyectos grandes es necesarios repartir
cada compente del codigo en diferenctes modulos asi no es facil que se
corronpa todo el proyecto si no solo un arhivo de este.
"""

#IMPORTAR TODO DEL MODULO

"""
importar todo un modulo - import + nombre del modulo - import estudiante

importar una clase - from  nombre modulo import nombre de la clase - from estudiante import Estudiante

se puede usar un alias para simplificar el nombre de el modulo o clase que vayamos a importar - import estudiante AS est

"""

#FUNCIONES PROPIAS 

"""
se puede crear utilidades.py con validar(), guardar(), buscar()

"""

# if __name__ == "__main__"

"""
esto sirve para que un archivo de python sepa como esta siendo ejecutado 
si se abre diectamente o si se abre desde otro archivo por medio de la importacion

¿como cambia el valor de __name__?
esto depende de como se ejecuta ek archivo

caso 1: ejecucion directa 
si en la terminal se escribe python main.py 
python entiende que es el archivo principal asi que en su interior le asigna el nombre 
especial "__main__"  
por lo tanto la condicion if __name__ == "__main__" se cumple y todo el codigo dentro
de ese bloque se va a ejecutar.

caso 2: IMPORTACION 

cuando desde un archivo se llama a otro python identifica que no se esta usando 
el archivo principal , si no que es una importacion , asi que asigna a __name__
el nombre real del archivo "main". 
Como "main" no es igual a "__main__" la condicion del if no se cumple , todo el codigo dentro de ese 
bloque se ignora por completo.

"""

#EJEMPLO 

def validar ():
    print("validando datos ...")

#codigo de prueba 
if __name__ == " __main__":
    print("se ejecutan directamente utilidades.py")
    validar()