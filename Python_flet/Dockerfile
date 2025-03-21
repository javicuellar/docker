FROM python:latest

LABEL Maintainer="Prueba docker python + flet"

# Con Python no hace falta instalar estos paquetes
# RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip  && apt-get clean  \
#  && rm -rf /var/lib/apt/lists/* 

# RUN apt-get install python3-venv

# Copiamos la aplicación al directorio /usr/src del contenedor
COPY . /usr/src

# Activamos como directorio de trabajo /usr/src
WORKDIR /usr/src
# Instalamos las dependencias necesarias para la aplicación
RUN pip install -r requirements.txt


# Ejecutamos la aplicación 
CMD ["/bin/bash"]



#  $ docker build -t python_flet:v0 .
#  $ docker run -it --name python_flet1 python_flet:v0						# Comando -it para arrancar bash (con -d no funcionaba).

#  $ docker run -it python:latest bash   									# Sin crear imagen, directamente de python


#  $ docker run -d -p 5010:5010 --name python_webapp prueba/python:1		# sin --netrower usa bridge, crea una nueva red interna   NO USAR
#  $ docker run -d --name python_webapp --network host prueba/python:1		# con --network host usa la misma IP						USAR
