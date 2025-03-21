#!/bin/bash

echo "Ejecutando el script de Alerta Madrid Digital"
python3 ./src/alertas.py &  


echo "Iniciando la aplicación web AppWebFinanzas"
python3 ./src/app.py &  


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."