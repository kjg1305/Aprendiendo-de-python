#EJERCICIO 1: USAR UNA API PUBLICA DE GEOLOCALIZACION  DE IPS ( ip-api.com -  ESTA NO REQUIERE RESGISTRO ),PARA PODER SABER EL ORIGEN DE UN IP "SOSPECHOSA"

import requests
#IP A REVISAR 
ip_revision="8.8.8.8"

# API 
url=f"http://ip-api.com/json/{ip_revision}"

#SE HACE LA PETICION A LA API
respuesta=requests.get(url)
datos=respuesta.json()

#ANALISIS DE LA RESPUESTA DE  SEGURIDAD LA API 
if datos ["status"]=="success":
    print(f"[RECONOCIMIENTO DE IP: {ip_revision}]")
    print(f" PAIS: {datos['country']}({datos['countryCode']})")
    print(f"PROVEERDOR DE INERNET (ISP): {datos['isp']}")
    print(f"ORGANIZACION: {datos['org']}")
else:
    print("NO SE PUDO OBTENER INFORMACION DE LA IP")



#EJERCICIO 2: AUTOMSTIZANDO UN ATAQUE DE FUERZA BRUTA A UNA API - ESENARIO SIMULADO DE HAKING ETICO
#SITUACION: UNA EMRPESA CREO UNA API PARA LOGEAR USUARIOS, PERO NO PUSO UN LIMITE DE USUARIOS (VULNERIVIDAD LLAMANDA IMPROPER RATE LIMITING), 
#SE VA A CREAR UN SCRIPT QUE INTENTE ADIVINAR LA CONTRASEÑA ENVIANDO PETICIONES POST REPETIDAS DE FORMA RAPIDA
#SE VA USAR UN SERVIDOR DE PRUEBAS DE INTERNET QUE VA A RESPONDER SIMULANDO EL COMPORTAMIENTO DE UNA API

import time
#URL DE API  DE AUTENTICACION QUE SE VA A AUDITAR
url_login="https://httpbin.org/post"

#EL USUARIO QUE YA SE CONOCE
usuario_objetivo="admin"

#DICCIONARIO DE CONTRASEÑAS (WORDLIST) DEBE SER UN ARCHIVO DE TEXTO CON MILES DE PALABRAS PERO PARA LA SIMULACION SE USA UNA LISTA 
diccionario_contraseñas=["123456","password","password123","qwerty","admin123","seguridad2026"]

#LA CONTRASEÑA REAL QUE SERVIDOR "ACEPTARIA"
contraseña_correcta="admin123"

#INICIO DE ATAQUE AL USUARIO OBJETIVO
print("INICO DE ATEQUE ")
#BUCLE QUE AYUDA A HACER LAS PETICIONES VARIAS VECES Y RAPIDO
for contraseña in diccionario_contraseñas:
    #datos que se enviaran en el json
    datos_login={
        "user":usuario_objetivo,
        "password":contraseña
    }

    #probando las contraseñas
    print(f"PROBANDO LA CONTRASEÑA : {contraseña}   ", end="")
    #envio de la peticion .post () con los datos
    respuesta=requests.post(url_login,json=datos_login)

    #simulacion de validacion del servidor
    if contraseña==contraseña_correcta:
     print("CONTRASEÑA ENCONTRADA")
     print(f"ACCESO CONCEDIDO CON LAS CREDENCIALES -> { usuario_objetivo}:{contraseña}")
     break
    else:
       print("INCORRECTA ")

    #AÑADIR UN SEGUNDO DE RETRASO PARA NO SATURAL EL SERVIDOR
    time.sleep(0.5)

print("ANALISIS FINALIZADO")