# jgiraldop-st0263
# info de la materia: st0263 <Topicos Especiales en Telematica>
#
# Estudiante(s): Julian Giraldo Perez, jgiraldop@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# Reto 2, uso de RPC y MOM 
#
# 1. breve descripción de la actividad
#
En esta actividad se implemento un apiGateWay, el cual resolvera ciertas consultas a traves de un middleware rpc y uno mom, que esta conectado a dos microservicios.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Entre los aspectos propuestos para la actividad se logro:
- Implementacion de apiGateWat
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
La siguiente explicacion se da como si se tuviera una instancia nueva de ubuntu en AWS.

## detalles del desarrollo.

Este proyecto esta pensado para correr en una maquina con linux, especificamente en una maquina ubuntu de AWS.

## detalles técnicos

El proyecto fue desarrollado en python 3.10.6.
La ApiGateWay se implemento utilizando Flask 2.2.3
Para la comunicacion grpc se utilizaron las librerias
- grpcio 1.51.3
- grpc-tools 1.51.3
Para la comunicaicon con rabbitmq se utilizo
- pika 1.3.1

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)
