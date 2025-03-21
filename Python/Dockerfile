FROM python:latest

LABEL Maintainer="Pruebas python"

# Con Python no hace falta instalar estos paquetes
# RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip  && apt-get clean && rm -rf /var/lib/apt/lists/*
#	&& apt-get install -y python3-venv \

# Copiamos la aplicación al directorio del contenedor
COPY . /usr/Python
COPY /Herramientas /usr/local/lib/python3.13/site-packages

# Activamos como directorio de trabajo
WORKDIR /usr/Python

# Instalamos las dependencias necesarias para la aplicación.
RUN pip install -r requirements.txt

# Exponer puerto
# EXPOSE 5010

# Definir volumen para persistencia de datos
VOLUME ["/usr/Python"]

# Ejecutamos la aplicación 
# CMD [ "./bin/sh"]



#  1) Crear Imagen - docker build --network host -t python_pruebas .

#  docker run -d --name AppWeb_alertas -v /volume1/Python_NAS/AppWeb_alertas:/usr/AppWeb_alertas -v /volume1/video:/video --network host appweb_alertas:0.4



# 2) Crear un contenedor de Python con Docker
# docker run --rm -it -v /volume1/Python_NAS/Python:/usr/Python --network host python /bin/sh

#    Desde el terminal, ecujetar:
#       cp -r Herramientas /usr/local/lib/python3.13/site-packages
