#!/bin/bash

echo "##############    selenium-scrapper    #############"
echo "Instalando las dependencias necesarias"
# pip install -r requirements.txt  > ./requirements.log
# sudo pip install --break-system-packages -r requirements.txt


# echo "Copiar scripts Herramientas"
# cp -r /usr/python/Herramientas /usr/local/lib/python3.13/site-packages


echo "Ejecutando el script main.py"
# python3 ./main.py 
python3 ./prueba.py 


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."