#HERRAMIENTAS DE PYTHON PARA MEJORAR LA ESCRITURA Y EFICANCIA DEL CÓDIGO
#NO ESENCIALES PERO SI UTILES

# 1.ENUMERATE ( EL CONTADOR AUTOMATICO)

"""
Cuando se usa un bucle for normal para revisar una lista ( con una lista de estudiantes)
Python da el elemento de la lista pera no el la pasición (índice) de ese elemento.
Normalmente, se tendría que crear una variable contador inicializada en 0 e ir sumandole 1 
en cada iteracion del buccle for. Enumerate() es una funcion que hace este trabajo aburrido 
y devuelve dos cosas al mismo tiempo: la posición (índice) y el elemento de la lista.
"""

#ejemplo:

estudiantes=["KAREN","CARLOS","DIANA"]

#enumerate() nos da el  indice (i) y el elemento (estudiante) de la lista estudiantes

for i,estudiante in enumerate (estudiantes):
    print(f"Estudiante numero {i+1} : {estudiante}")

# 2. LIST COMPREHENSION (LISTAS EN UNA SOLA LINEA)

"""
Cuando se tiene una lista de objetos y solo se quiere extraer sus nombres para meterlos
en una lista nueva la forma tradicianal seria:

nombres=[]

for e in estudiantes:
    nombres.append(e.nombre)

la list comprehension es solo un atajo para escribir exactamente lo mismo pero dentro de 
los corchetes [] de la nueva lista. Se lee de atras hacia adelante:     
"""
nombres=[e.nombres for e in estudiantes ]
#crea una lista gaurdando e.nombre para cada elemento e en la lista estudiantes.

#LAMBDA ( FUNCIONES MINIATURA O DESHECHABLES)

"""
Una funcion normal en python se crea con def. Pero aveces se necesita una mini funcion que 
solo hace una operacion matematica o develve un dato basico, y te da pereza crear todo un 
def para usarla una sola vez. Eso es una funcion Lambda.
"""
#forma tradicional 
def obtener_nombre(x):
    return x.nombre

#forma con Lambda 
lambda x:x.nombre

"""
Las lambdas no llevan def , no llevan return y no tiene nombre. Se usan mucho cuando 
se queire ordenar una lista de objetos. 
"""

#DICCIONARIOS ( ESTURCTURAS DE CLAVE - VALOR )

"""
A  diferencia de las listas donde accedes a los datos por su posicion numerica, en un diccionario 
se accede a los datos mediante una CLAVE (una palabra) y se abre con llaves{}.

"""
#diccionario
estudiante ={
    "nombre" : "karen", 
    "edad":19
}
#obtener el dato
print (estudiante["nombre"]) #karen
print (estudiante["edad"]) #19


#JSON ( IDIOMA UNIVERSAL DE LOS DATOS )

"""
JSON significa JavaScripy Object Notation, es un formato de datos universal 
que se usa para intercambiar datos entre sistemas (simplemente texto plano estructurado).

En Python JSON es identico a un diccionario de Python. Cuando se corre un programa se usa un diccionario  
y cuandos se guarda ese diccionario en el disco duro para que no se borre se convierte en JSON(texto plano) 
y cuando se vuelve a cargar en el programa se convierte de nuevo en un diccionario de Python.

"""

#¿COMO SE ESTRUCTURA UN ARCHIVO JSON ?
"""
Utiliza llavez {} para los objetos (equivalente a diccionarios ) y corchetes [] para las listas.

"""
#ejmplo

{
    "universidad": "UNAM",
    "sede":"ciudad",
    "activa":true,
    "lista esudiantes":[
        {
            "nombre":"anita",
            "edad":20,
            "materias":["POO","Matematicas","Fisica"]
        },
        {
            "nombre":"carlos",
            "edad":21,
            "materias":["PYTHON","DATA BASES"]
        }
    ]
}

#REGLAS DE JSON ( DIFERENCIAS CON PYTHON )

"""
1.Las comillas dobles "" son obligatorias para las claves y textos ,
 si se usan comillas simples '' el archivo JSON no es valido y se rompe.
2.los valores booleanos se deben escribir en minusculas true y false, 
no True y False como en Python.
3. JSON no permite comentarios, si se ponen comentarios el archivo 
JSON no es valido y se rompe.

"""

#JSON EN PYTHON COMO FUNCIONA 
"""
Python ya cuenta con el modulo de json que perimte manjarlo, se deven aprender 
fundamentalmente dos funciones: 

json.dump() : traducir de python a archivo JSON, toma un diccioanrio o lista de python
y lo escribe en un archivo de texto plano con formato JSON.

json.load(): traducir de archivo JSON a python, lee el archivo de texto y
lo convierte automaticamente en dicionario o lista de python utilizables.

"""

#ejemplo 1 guarda tus datos (escritura)

import json

#tus datos en un diccionario de python
datos_consola = {
    "nombre":"karen",
    "edad":20,
    "curso":"aprendiendo python"
}
#se abre o crea un archivo de JSON "progreso.json" en modo escritura "w"
with open ("progreso.json","w",encoding ="utf-8") as archivo:
    #json.dump toma el dicionario, archivo y indent =4 para que se vea bonito y ordenado.
    json.dump(datos_consola,archivo,indent=4)

print ("Datos con exito en progreso.json")

# ejmplo 2 recuperar datos al abrir la app (lectura)

import json 

#Abrir el archivo en modo lectura "r"
with open ("progreso.json","r",encoding="utf-8") as archivo:
    #json.load lee el archivo y lo convierte en un diccionario de python
    datos_cargados=json.load(archivo)
#ahora se puede usar como cualquier diccioanrio normal de python 
print (datos_cargados)

#JSON es mucho mas eficiente que usan archivos .txt 
# porque no hay que hacer conversiones de texto a datos, y es mucho mas eficiente
# que usar archivos .csv porque permite guardar listas y diccionarios anidados.