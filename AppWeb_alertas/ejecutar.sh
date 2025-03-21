#!/bin/bash

echo "#################################################"
echo "Instalando las dependencias necesarias"
pip install -r requirements.txt  > ./log_install_requerimientos.log


echo "Ejecutando el script de Alertas: CONTROL ACCESO, Madrid Digital y tamaño ficheros"
python3 ./src/alertas.py 


echo "Iniciando la aplicación web AppWebFinanzas"
python3 ./src/app.py


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."