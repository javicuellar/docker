#!/bin/bash

echo "##############    AppWeb_contactos    #############"
echo "Instalando las dependencias necesarias"
cd ./Appweb_contactos
pip install -r requirements.txt  > ./requirements.log


# echo "Copiar scripts Herramientas"
# cp -r /usr/python/Herramientas /usr/local/lib/python3.13/site-packages


echo "Iniciando la aplicación web Appweb Contactos"
python3 ./run.py


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."