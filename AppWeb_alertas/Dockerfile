FROM python:latest

LABEL Maintainer="App Web + Alertas v0.4"
#  Versión 0.2 - Se incluye alerta puestos en Madrid Digital, ejecutándolos en dos scripts diferentes.
#  Versión 0.3 - Se incluye alerta ficheros grandes
#  Versión 0.4 - Actualización de Herramientas, copiadas al path de librerías de Python

# Con Python no hace falta instalar estos paquetes
# RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip  && apt-get clean && rm -rf /var/lib/apt/lists/* && apt-get install -y python3-venv \

# Copiamos la aplicación al directorio del contenedor
COPY . /usr/AppWeb_alertas

# Activamos como directorio de trabajo
WORKDIR /usr/AppWeb_alertas

# Instalamos las dependencias necesarias para la aplicación.
# RUN pip install -r requirements.txt
# Se insltalan desde el ejecutable  "ejecutar.sh"

# Exponer puerto
# EXPOSE 5010

# Definir volumen para persistencia de datos
VOLUME ["/usr/AppWeb_alertas", "/video"]

# Ejecutamos la aplicación 
CMD [ "./ejecutar.sh"]




#  CREAR IMAGEN - docker build --network host -t appweb_alertas:0.4 .


#  docker run -d --name AppWeb_alertas0.4 -v /volume1/Python_NAS/AppWeb_alertas:/usr/AppWeb_alertas -v /volume1/video:/video --network host appweb_alertas:0.4