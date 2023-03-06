# jgiraldop-st0263
## info de la materia: st0263 Topicos Especiales en Telematica
#
## Estudiante(s): Julian Giraldo Perez, jgiraldop@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# Reto 2, uso de RPC y MOM 
#
# 1. breve descripción de la actividad
#
En esta actividad se implemento un apiGateWay, el cual resolvera ciertas consultas a traves de un middleware rpc y uno mom, que esta conectado a dos microservicios.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Entre los aspectos propuestos para la actividad se logro:
- Implementacion de apiGateWay
- Implementacion de comunicacion via GRPC de ApiGateWay con microservicio
- Implementacion de comunicacion via MOM de apiGateWay con microservicios (Se realizo con rabbitmq y el uso de colas)
- Balanceador de carga dentro del apiGateWay
- Aplicacion de tolerancia a fallos en el apiGateWay
- Creacion de script para correr todos los archivos necesarios

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- Implementacion de bootstrap en AWS.
  Se encontraron problemas a la hora de ejecutar comandos utilizando el user Data en AWS. En mi caso particular el error consistia en que no podia utilizar las librerias de mis archivos de python.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

En general el diseño de esta aplicacion va de acuerdo a lo propuesto en clase
![image](https://user-images.githubusercontent.com/110442546/223032463-19a8c258-d060-45c5-a541-3ac6355a4722.png)

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.
Para complilar y ejecutar el programa primero se debe correr el script install.sh, de esta forma se instalaran todas las dependencias. Ademas en AWS se debe habilitar el puerto 8080 por TCP desde cualquier IP. 

Posteriormente se debe correr el script run.sh, el cual correra todas los archivos de python requeridos

## detalles del desarrollo.

Este proyecto esta pensado para correr en una maquina ubuntu de AWS.

## detalles técnicos

El proyecto fue desarrollado en:
- python 3.10.6.
La ApiGateWay se implemento utilizando:
- Flask 2.2.3
Para la comunicacion grpc se utilizaron las librerias
- grpcio 1.51.3
- grpc-tools 1.51.3
Para la comunicaicon con rabbitmq se utilizo
- pika 1.3.1

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
En general se tiene un archivo de configuracion para al API gateway y para cada microservicio.
### gateWay
- request_queue: Nombre cola de peticion
- response_queue:Nombre cola de respuesta
- rpc_port: puerto para la conexion rpc
- rpc_address: direccion para la conexion rpc
- server_port: Puerto en que se despliega el servidor
- server_address: Direccion donde se despliega el servidor

### RPC microservice
- rpc_port: Puerto para la conexion rpc
- dir_path: path del directorio que posee los archivos

### MOM microservice
- queue: Nombre de la cola a la que escucha
- dir_path: path del directorio que posee los archivos

## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
En general el proyecto esta pensado para ser clonado en la direccion /home/ubuntu/
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 
### Estructura
![image](https://user-images.githubusercontent.com/110442546/223045303-ccc8f88c-aaa0-4e1f-ac92-a898ded7eff8.png)

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.
18.210.179.173
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
En el numeral anterior ya se describieron todos los parametros y configuraciones del apigateway y de cada mciroservicio. 
Cabe destacar que estos ya vienen configurados predeterminadamente

## como se lanza el servidor.
- Asegurarse de tener el puerto 8080 abierto para comunicacion TCP desde cualquier ip
- git clone de este repositorio
- Correr install.sh (Ubicado en la carpeta fuente del git)
- Correr run.sh (Ubicado en la carpeta fuente del git)

## una mini guia de como un usuario utilizaría el software o la aplicación
Para que el usuario pueda acceder a los endpoints debe poner la ip y el puerto correspondiente. Ej. http://18.210.179.173:8080/listFiles
### Explicacion balanceador
En este proyecto se tienen 3 microservicios, la idea es que se ira haciendo un balanceo entre el uso de los 3, por esto cuando se hagan peticiones se mostrara el origen de la respuesta (rpc, mom1, mom2) todo con el fin de comprobar este balanceo

### Endpoints

El usuario posee multiples endpoints para probar la aplicacion.

NOTA: Hay mas endpoints implementados en la aplicacion pero estos se hicieron con fines de testing. como (testRPC/, textMOM/, getFileMOM/<string>, getFileRPC<string>)

- /listFiles: Lista los archivos del microservicio
- /getFiles/<string: dir>: obtiene archivos que tengan cierto nombre (no incluir extensiones). Para buscar dentro de carpetas usamos la sintaxis carpeta.archivo
- /: Nos retornara alive si el servidor esta vivo


## opcionalmente - si quiere mostrar resultados o pantallazos 
![image](https://user-images.githubusercontent.com/110442546/223050778-5906d50a-f159-45bc-b136-e1961df68af2.png)
![image](https://user-images.githubusercontent.com/110442546/223050815-af2bfde8-7572-4e27-ab5c-8b21c6ba36b2.png)
![image](https://user-images.githubusercontent.com/110442546/223050854-79737619-b080-424b-91bd-7903596f7de4.png)
![image](https://user-images.githubusercontent.com/110442546/223051939-b753c079-269a-4743-95b6-5c9028a6ede6.png)
![image](https://user-images.githubusercontent.com/110442546/223051975-97bb17c0-c995-4b4f-9cf2-fa19cee56430.png)


# 5. otra información que considere relevante para esta actividad.
Todo lo relevante para esta actividad ya esta contenido en los otros numerales

# referencias:

## https://www.rabbitmq.com/getstarted.html
## https://grpc.io/docs/languages/python/quickstart/

#### versión README.md -> 1.0 (2022-agosto)
