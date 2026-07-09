##ARCHIVOS-----------------------------------------------------------------------------------

##COMO GUARDAR TEXTO 

with open ("datos.txt", "w") as archivo:
    archivo.write("Holii")
""""
##para poder agragar texto en un archivo sin borrar la informacion que 
ya tiene , se usa el modo "a" en lugar de "w" , esto se conoce como modo
de apertura de archivos , 

## el modo"w" es para escribir en un archivo
## el modo "wirteLines" escribe varias lineas
## el modo "a" es para agregar texto a un archivo al final  sin borrar la informacion que ya tiene , 
##el modo "r" es para leer un archivo 
## el modo "readLine "  lee una linea 
## el modo "readLines" devuelve una lista de lineas
##el modo "r+" es para leer y escribir
## el modo "x" es para crear un nuevo archivo y ya existe el archivo da error.
## el modo "b" es para abrir un archivo en modo binario el cual es mejor para manipular imagenes,
audios , PDFs o ejecutables , "rb" lee el archivo en formato de bytes y "wb" escribe bytes puros 
que sirve para descargar una imagen en internet y guardarla en el disco por ejemplo.
## el modo "t" es para abrir un archivo en modo texto , por defecto se abre en modo texto.

##el with ayuda mucho para cuando se olvida cerrar el archivo
en el with crear un bloque protegido y no importa lo que pase adentro python garantiza
que al salir de ese bloque el archivo se cerrara solo 

#FORMA INSEGURA 
archivo =open ("datos.txt","r")
si aqui ocurre un error , el archivo se quda abierto en memoria 
contenido=archivo.read()
archivo.close()


"""
# COMO LEER UN ARCHIVO  

with open ("datos.txt","r") as archvio:
  #  print (archivo.read())
  pass # para no error

"""
cada parte de la sintaxis del with es simple , with le dice a python "abre este bloque y cierralo 
al final , open (..) es el que abre el archivo y as Archivo es solo el nombre de la variable
que se elige para iteracturar con ese archivo dentro del bloque en si esa variable como cualquiera
puede tener cualquier nombre.

"""
## para leer archivos grandes es mejor iterar linea por linea , lo cual es muy eficiente
##por que python solo mantiene una linea de codigo a la vez en la memoria.

with open ("archivo_gigante.txt","r")as archivo:
    for linea in archivo:
        print(linea.strip()) # el .strip() quita los saltos de linea \n extra.

##MANEJO DE  ERRORES 

#cuando se intenta abrir un archivo con "r" pero el archivo no existe , el programa
# se va a romper con un error en la ejecucion 
#para evitar esto se debe protejer ese bloque de codigo con try-except

try:
    with open ("no_existo.txt","r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("el archivo no existe en la carpeta verifica el nombre")

##se puede usar cualquier extencion de archivo de texto plano .py . java etc.

#EL METODO SPLIT()

"""
Cunado se lee una linea de un archivo (como un archivo csv), los datos suelen venir todos 
juntos en una solo cadena de texto , separados por un caracter.
El metodo .split("caracter") toma esa cadena y la "corta" cada vez que encuentra un "caracter"
Al hacerlo , te devulve una lista con los elementos separados 

"""
#ejemplo

linea = "1;karen;20;4.5"
datos= linea.split(";")
print (datos)
#resultado : [´1´,´karen´,´20´,´4.5´]


#COVERSION DE TIPOS 
"""
todo lo que se lee de un archivo entra como un texto (String) incluso si hay numeros
si se mira en el tema anterior cuando se quita el caracter ";" de la linea los numeros se deuelven 
con comillas incdicando que son cadenas de texto y por lo tanto no se puede hacer operaciones matematicas, 
si se intenta hacer "20" + 5 el programa va a fallar. 
Para solucionar eso se necesita "trasformar" o convertir  los datos a su tipo correcto
--int() converte texto a numeros enteros decimales y -- float() convierte texto a numeros con decimales.

"""
#EJEMPLO

datos=["1","karen","20","4.5"]
#convertir cada elemeto segun corresponda
id_estudiante=int(datos[0])
nombre=datos[1]
edad=int(datos[2])
nota=int(datos[3])

#ahora que ya se convertieron los valores si se pueden hacer matematicas
print(edad+1)
print(nota*2)

#--------------------------------------------------------------------------------
##ejercicio 
##crear un programa que pida nombre y los guarde en un archivo y luego que lo lea

nombre = input("Ingrese un nombre :")
nombre2=input ("Ingrese un segundo nombre : ")

with open ("archivo_nombres.txt","w") as nombres:
    nombres.write(nombre+"\n")
    nombres.write(nombre2+"\n")

with open ("archivo_nombres.txt","r") as nombres_leidos:
    print(nombres_leidos.read())