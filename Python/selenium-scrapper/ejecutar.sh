#!/bin/bash

echo "##############    selenium-scrapper    #############"
echo "Cambiar de directorio, si se ejecuta desde Python"
cd /usr/python/selenium-scrapper

echo "Actualizamos pip"
pip install --upgrade pip
wait

echo "Instalando las dependencias necesarias"
pip install -r requirements.txt  > ./requirements.log
wait


echo "Copiar scripts Herramientas"
cp -r /usr/python/Herramientas /usr/local/lib/python3.13/site-packages
wait

echo "Esperamos a que se cargue el contenedor de selenium"
sleep 150
# echo "Ejecutando el script python"
# python3 ./prueba.py 
# wait
# python3 ./alerta_esqui.py 
python3 ./prueba1.py


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."