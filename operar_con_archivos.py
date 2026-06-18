##ARCHIVOS

##COMO GUARDAR TEXTO 

with open ("datos.txt", "w") as archivo:
    archivo.write("Holii")

## para poder agragar texto en un archivo sin borrar la informacion que 
##ya tiene , se usa el modo "a" en lugar de "w" , esto se conoce como modo
## de apertura de archivos , 
# el modo"w" es para escribir en un archivo
## el modo "a" es para agregar texto a un archivo sin borrar la informacion
## que ya tiene , 
# el modo "r" es para leer un archivo 
## el modo "x" es para crear un nuevo archivo.
## el modo "b" es para abrir un archivo en modo binario el cual es mejor para manipular imagenes,
#audios , PDFs o ejecutables , "rb" lee el archivo en formato de bytes y "wb" escribe bytes puros 
#que sirve para descargar una imagen en internet y guardarla en el disco por ejemplo.
# el modo "t" es para abrir un archivo en modo texto , por defecto se abre en modo texto.


# COMO LEER UN ARCHIVO  

with open ("datos.txt","r") as archvio:
  #  print (archivo.read())
  pass # para no error

## para leer archivos grandes es mejor iterar linra por linea , lo cual es muy eficiente
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


##ejercicio 
##crear un programa que pida nombre y los guarde en un archivo y luegoq que lo lea

nombre = input("Ingrese un nombre :")
nombre2=input ("Ingrese un segundo nombre : ")

with open ("archivo_nombres.txt","w") as nombres:
    nombres.write(nombre+"\n")
    nombres.write(nombre2+"\n")

with open ("archivo_nombres.txt","r") as nombres_leidos:
    print(nombres_leidos.read())