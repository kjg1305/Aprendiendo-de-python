#EXEPCIONES 

#TRY 
"""
se pone a prueba el codigo que puede tener o generar un error 
"""
#EXCEPT
"""
Para atrapar el error si ocurre , y indicar que hacer si ocurre el error.
"""

#FINALLY 
"""
se pone el codigo que se ejecute pase lo que pase 
A direfencia de EXCEPT  (  que solo corre si hay un error )
el blqoue Finally se va a ejcutar siempre sin importar si el codigo funciono 
a la perfeccion o si exploto por completo.

Se usa pirncipalmente para tareas de limpieza, como cerrar un archivo,desconectarse de una base de datos
o cerrar una ventana del navegador , asegurando que los recursos no se queden
desperdiciados en la memoria.

"""

#EJEMPLO

try :
    print ("Abriendo la base de datos ...")
    resultado=10/0 # esto da una excepcion 
except ZeroDivisionError:
    print("NO se puede dividir por cero ")
finally :
    print("Cerrando la base de datos ...")


#RAISE 

"""
Para forzar o lanzar errores propipios 

algunas veces una linea de codigo es completamnete valida por python 
pero para la Logica del programa es una error, Raise permite activar 
la alarma de forma voluntaria y detener el programa con una excepcion especifica.

Esto ayuda a validar condiciones. Si un usuario introduce un dato que 
no tiene sentido logico (como una edad negativa ) , se puede lanzar un error 
antes de que el programa continue y haga desastres.

"""

#EJEMPLO 

def resgistrar_edad(edad):
    if edad<0:
        raise ValueError("La edad no puede ser negativa")
    print(f"Edad registrada: {edad}")

#Probando la funcion

try: 
    resgistrar_edad(-5)
except ValueError as error :
    print(f"Error atrapodo: {error}")