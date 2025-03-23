#!/bin/bash

echo "############   appweb_flask_SQLite   #############"
echo "Instalando las dependencias necesarias"
cd ./appweb_flask_SQLite
pip install -r ./requirements.txt  > ./requirements.log


echo "Copiar scripts Herramientas"
cp -r /usr/python/Herramientas /usr/local/lib/python3.13/site-packages


echo "Iniciando la aplicación web"
python3 ./webapp.py


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."