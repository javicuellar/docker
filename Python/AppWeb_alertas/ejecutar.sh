#!/bin/bash

echo "#################################################"
echo "Instalando las dependencias necesarias"
cd ./AppWeb_alertas
pip install -r requirements.txt  > ./requirements.log


echo "Copiar scripts Herramientas"
cp -r /usr/python/Herramientas /usr/local/lib/python3.13/site-packages


echo "Ejecutando el script de Alertas: CONTROL ACCESO, Madrid Digital y tamaño ficheros"
python3 ./src/alertas.py 


echo "Iniciando la aplicación web AppWebFinanzas"
python3 ./src/app.py


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."