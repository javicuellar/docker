# INSTRUCCIONES BASICAS DE DOCKER

-------------------------------------------------------------------------------------------------

* Acceso vía SSH
    - ssh Javi@192.168.1.41        (hay que indicar usuario@IP)

* Elevar permisos para ejeucator comandos de docker
    - sudo -i

--------------------------------------------------------------------------------------------------

# **Crear Imagen**



# **Crear Contenedor** 

*Python*

	*simple* - docker run --name python_pruebas -d -it python:latest /bin/bash
	*volumen* - docker run --name python_pruebas -d -it -v /volume1/Python:/usr/python python:latest /bin/bash


*Contenedor Multiproposito python*

	docker run -d -it --name NasPython -v /volume1/Python:/python -v /volume1/video:/video python:latest /python/lanzador.sh

*Crear contenedor con Dockerfile*

	"Desde la carpeta donde se encuentra el fichero Dockerfile, ejecutar:"
	docker build -t prueba/python:1

*Crear contenedor con docker-compose.yaml"

	- Crear carpeta en docker, "contenedor", y en ella carpeta config"
	- Desde synology se crea proyecto, indicando carpeta y automáticamente coge el docker-compose.yaml.
	- Se puede crear el docker-compose a partir de la instrucción docker run ... usando las webs:
		https://docker-compose.net    o    https://www.composerize.com

-------------------------------------------------------------------------------------------------

Desde la consola del NAS

	Crear contenedor 
	- Imagen (python:latest), nombre contenedor
	- volumen: agregar tantos como se necesiten. Agregar carpeta del NAS y mapear en contenedor (/video)
	- configurar red si es necesario
	- Orden de ejecución: Entrypoint o comando (/bin/bash para el terminal) 

	* Una vez creado, tiene una opción para arrancar el terminal.

Desde consola NAS, crear proyecto con docker-compose

	- Ver más arriba en docker-compose.



## Pruebas
-----------------------------------------------------------------------------------------------------

*AppWebFinanzas_Alertas*

	**Crear imagen desde Docerfile** - docker build -t appwebfinanzas_alertas:0.3 .

	**NO USAR**.- sin --netrower usa bridge, crea una nueva red interna
	docker run -d -p 5010:5010 --name AppWebFinanzas appwebfinanzas_alertas:0.3

	**USAR**.-  con --network host usa la misma IP
	docker run -d --name AppWebFinanzas_alertas -v /volume1/Python/AppWebFinanzas_alertas:/usr/AppWebFinanzas_alertas --network host appwebfinanzas_alertas:0.3
	

### Pruebas Docker en Windows
------------------------------------------------------------------------------------------------------

*NO FUNCIONA si no haces login*

	docker login --username javicuellar     **(informar password cuando la pida "D simple 5")**

#### Pruebas

*Windows* -	docker run --name windows -d -it -p 80:80 dockurr/windows:latest

	Error: docker: no matching manifest for windows/amd64 10.0.22631 in the manifest list entries.	??
