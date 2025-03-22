#!/bin/bash

echo "#################################################"
echo "Instalando las dependencias necesarias"
cd ./appweb_flask_upload_file
pip install -r ./requerimientos.txt  > ./requerimientos.log


echo "Copiar scripts Herramientas"
cp -r /usr/python/Herramientas /usr/local/lib/python3.13/site-packages


echo "Iniciando la aplicación web"
python3 ./app.py


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."