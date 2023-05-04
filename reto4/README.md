# jgiraldop-st0263
## info de la materia: st0263 Topicos Especiales en Telematica
#
## Estudiante(s): Julian Giraldo Perez, jgiraldop@eafit.edu.co
#
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# Reto 4, Moodle GCP
### Link del proyecto
https://www.devjgp.tech/


# 1. Actividad
En este reto se desarrollo el montaje de una arquitectura con Moodle, la cual cuenta con 4 elementos principales.

- GCP Balanceador de carga: Este balanceador es el encargado de distribuir la carga a traves de las instancias de moodle ubicadas en el grupo de instancias, ademas este tambien gestiona los certificados SSL. Cabe destacar que la IP de este balanceador es la que esta en los registros DNS del dominio

- Grupo de instancias: Este es un servicio de GCP el cual nos permite tener un grupo de instancias derivadas de la misma imagen de instancia. 

- GCP SQL: Servicio de GCP el cual contiene la base de datos a utilizar.

- GCP Filestore: Servicio de GCP el cual actua como servidor NFS, desde el cual se compartiran archivos a diferentes instancias.

## A tener en cuenta
Para el desarrollo de esta actividad se utilizaron diferentes servicios de GCP, y ademas, se utilizo el contenedor bitnami/moodle para facilitar el despliegue de la aplicacion de moodle a traves de las instancias. Dentro de estas mismas instancias se realizo la configuracion correspondiente al cliente NFS.


Finalmente, para obtener el dominio se utilizo la pagina hostinger, desde la cual tambien se hace el manejo del DNS, en este caso para la configuracion del DNS se hizo un registro A que apunta a la ip del balanceador de carga.

## 1.1 Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
En esta actividad se logro:
- Utilizar y configurar correctamente el servicio de GCP filestore para la configuracion tanto del cliente como del servidor NFS.

- Utilizar y configurar GCP SQL para que esta base de datos fuera usada por los contenedores de moodle 

- Configurar el grupo de instancias para implementar crecimiento horizontal en autoscaling

- Configurar y utilizar el servicio de balanceo de carga de GCP, para que este distribuyera la carga sobre el grupo de instancias

- Configurar el certificado SSL para que funcionara con el balanceador de caraga de GCP

- En cuanto a los requisitos no funcionales, gracias a todo lo implementado se logro el principal requisito que iba enfocado a la alta disponibilidad. 


## 1.2 Que aspectos no cumplió o no desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
De forma general se lograron todos los items propuestos en la actividad.

# 2. Informacion general de diseño de alto nivel y arquitectura

![reto3 drawio](https://user-images.githubusercontent.com/110442546/235377747-766208ac-4b3b-4d61-b016-8591efa9dbb7.png)


Como se ve en la imagen la arquitectura del proyecto se divide de forma en general en 5 cajas, las cuales analizaremos de arriba a abajo.
Primero tenemos Hostinger, aqui es donde se realizo la gestion del dominio y del DNS, alli es donde tenemos el registro que apunta a nuestro balanceador de carga, el cual se encarga de distribuir el flujo del trafico a travez de las instancias dentro del grupo de instancias. El numero de instancias dentro del grupo pueden aumentar o disminuir dependiendo de la carga que hay sobre las diferentes instancias. Por ultimo cada instancia de este grupo esta conectada al GCP SQL para el manejo de la base de datos y al GCP Filestore para el manejo de los archivos compartidos (NFS)


# 3. Descripcion del ambiente se desarrollo y tecnico 
Para el desarrollo de la actividad se utilizo:

- Maquinas virtuales micro de gcp con 10gb de almacenamiento y ubuntu 20.04 

- Docker para correr Moodle 

- GCP Load Balancer para balancear la carga

- Imagenes de instancias para poder construir templates de instancias

- Templates de instancia para a paritr de estas crear el grupo de instancias

- Grupo de instancias para ejecutar el auto scaling sobre estas.

- Para crear el sistema de archivos compartidos se utilizo Filestore como servidor NFS

- Para la gestion de la base de datos se utilizo GCP SQL

## Compilacion y ejecucion

### Base de datos

Dirigirse al servicio de SQL en GCP y crear una nueva instancia, asegurese de que esta sea una instancia de SQL.

una vez creada la instancia cree una nueva base de datos, posterior a esto debera ir a la configuracion de red de la instancia para permitir el acceso a la base de datos desde cualquier direccion IP (no recomendado para produccion).

### Filestore 

Crear instancia de Filestore (Cuidado pues esta consume muchos creditos)


### Maquinas virtuales

### Docker

Cree una nueva maquina virtual

Para instalar docker debe correr en su maquina

        sudo apt update
        sudo apt install docker.io -y
        sudo apt install docker-compose -y
        sudo apt install git -y

        sudo systemctl enable docker
        sudo systemctl start docker
        sudo usermod -a -G docker <username>
        
Para correr un archivo docker-compose correr

        docker-compose -f <nombre de archivo> up
        
### NFS Client

Primero instale NFS en su cliente

        sudo apt-get -y update &&
        sudo apt-get install nfs-common
       

Ahora cree el directorio donde querra montar los archivos del NFS server

        sudo mkdir /mnt/filedir/

Una vez realizado esto modificaremos el archivo fstab, para que de esta forma se configure todo lo relacionado al NFS cuando se inicie la maquina

        sudo nano /etc/fstab

Para ver en detalle lo que se ingresa en este archivo remitirse al documento nfs.txt presente en este repositorio.



### Docker-Compose
Una vez instalado docker, clone este repositorio y corra el docker compose, tenga en cuenta que debera cambiar algunas variables de entorno como el host de la base de datos, la contraseña, la localizacion del volumen, entre otras, para que todo sea congruente con su implementacion.


### Imagenes GCP

Una vez configurada la instancia se procedera a crear una imagen de la misma. 

### Instance Templates GCP

Cuando se tenga la imagen creada, cree un instance template a partir de la misma

### Grupo de instancias GCP

Con la instance Template se creara un grupo de instancias, la configuracion de este grupo queda a disposicion del lector.

### Balanceador de carga GCP

Se crea el balanceador de carga, utilizando como backend el grupo de instancias. Ademas para el front se importa un certificado SSL.

### DNS 

    1. Comprar un dominio en hostinger
    2. Crear un A register apuntando a la ip publica del balanceador
    


## Detalles del desarrollo
Para el desarrollo de este reto se comenzo por estudiar los diferentes servicios de GCP que eran necesarios para el desarrollo del proyecto, y ademas se reviso en docker hub como funcionaba la imagen de bitnami moodle. Posteriormente se comenzo por instanciar solo una maquina virtual, donde estaba todo Moodle de forma monolitica.

Luego de esto se comenzo a "distribuir" esta aplicacion monolitica, primero se creo uns instancia de GCP SQL, y se configuro el docker-compose de tal forma que se utilizara esta instancia de GCP SQL.

Posterior a esto se creo la instancia de GCP Filestore, y se hizo toda la configuracion en la maquina virtual para que esta funcionara como cliente NFS, ademas nuevamente, se altera el docker-compose para que el volumen apuntara al directorio montado.

Luego, se realiza primero una imagen de la instancia que tiene todo configurado, para a partir de esta crear una template de instancia. Con esta template se procede a crear un grupo de instancias y dentro de esta se definen diferentes parametros como el autoscaling. Para finalmente configurar el balanceador de carga, para que este distribuya el trafico a traves de las diferentes instancias del grupo.

Cuando ya se tuvo todo configurado y funcionando se utilizo un dominio de hostinger, y se realizo un registro A apuntando a la ip publica del balanceador de carga, de esta forma se completo la configuracion del Dominio, en el momento en que el dominio esta configurado se procede a generar los certificados SSL.

## Detalles tecnicos

Para el desarrollo del proyecto se utilizo:

- GCP Filestore
- GCP SQL
- GCP Virtual Machines
- GCP instance Group
- GCP load balancer
- Hostinger


## Configuracion y los parametros del proyecto

Las maquinas virtales se crearon con los siguientes parametros:
- SO ubuntu 20.04
- Maquina tipo micro 
- Para evitar posibles fallos habilitar comunicacion http y https3

Para la base de datos se utilizaron los parametros que consumieran menos recursos, ademas se configuro la conexion de tal manera que se puediera realizar una conexion desde cualquier IP

Para el filestore se utilizaron los parametros que consumieran menos recursos.

Para el grupo de instancias se tuvieron los siguientes parametros:

- AutoScaling: 1 - 4
- Scaling: Cuando superara el 60% de utilizacion de CPU

Para el balanceador se configuro que el backend fuera el grupo de instancias anteriormente creado, y para el front se configuro el Dominio y se importo un certificado SSL creado anteriormente. (En caso de que no lo tenga se recomienda usar certbot)


## ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO
## Estructura de directorios y archivos importantes del proyecto
En este proyecto no hay una estructura de directorios fija ya que todo se distribuyo a traves de diferentes maquinas y servicios.

#4. Descripción del ambiente de EJECUCIÓN (en producción)


## IP o nombres de dominio en nube o en la máquina servidor
Para facilitar el acceder a la pagina, se utilizo un dominio el cual esta configurado para que apunte a la ip publica del Nginx-server. 

        devjgp.tech
        www.devjgp.tech

## Como se lanza el servidor.

Simplemente se debe revisar que el GCP SQL y el balanceador de carga esten encendidos, ya que ni el grupo de instancias ni el filestore se pueden apagar.

Si todo esta montado ya deberia estar funcionando perfectamente

## Guia de como el usuario utilizaria el software o la aplicacion

Para utilizar la aplicacion el usuario simplemente debe ingresar a la url: jgpdev.tech

## Resultados o Pantallazos
![image](https://user-images.githubusercontent.com/110442546/235378736-be22e8f5-bfcc-44f8-9dc0-693b241e3125.png)
![image](https://user-images.githubusercontent.com/110442546/235378752-fe11315e-5f9f-446b-8f80-d3385e3387d7.png)
![image](https://user-images.githubusercontent.com/110442546/235378765-8beedc9f-37fe-4131-a819-2a725d22ed0a.png)
![image](https://user-images.githubusercontent.com/110442546/235378789-cc9c8bd6-4acd-42ba-8260-3ec00ea063fb.png)
![image](https://user-images.githubusercontent.com/110442546/235378812-d40b2bd4-cda7-4f7b-843d-678a39852c94.png)


# 5. otra información que considere relevante para esta actividad.

Este proyecto ya no esta desplegado debido a que este consumia demasiado creditos de GCP

# Referencias
- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-20-04
- https://cloud.google.com/filestore/docs/mounting-fileshares
- https://github.com/st0263eafit/st0263-231
- https://www.geeksforgeeks.org/how-to-create-a-load-balancer-on-gcp/


# URL
https://www.devjgp.tech/

# Video
https://youtu.be/mhHFo52om7k

