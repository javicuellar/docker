#!/bin/bash


echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | \
    tee -a /etc/apt/sources.list.d/google.list && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | \
    apt-key add - && \
    apt-get update && \
    apt-get install -y google-chrome-stable libxss1

BROWSER_MAJOR=$(google-chrome --version | sed 's/Google Chrome \([0-9]*\).*/\1/g') && \
    wget https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${BROWSER_MAJOR} -O chrome_version && \
    wget https://storage.googleapis.com/chrome-for-testing-public/`cat chrome_version`/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/bin/ && \
    DRIVER_MAJOR=$(chromedriver --version | sed 's/ChromeDriver \([0-9]*\).*/\1/g') && \
    echo "chrome version: $BROWSER_MAJOR" && \
    echo "chromedriver version: $DRIVER_MAJOR" && \
    if [ $BROWSER_MAJOR != $DRIVER_MAJOR ]; then echo "VERSION MISMATCH"; exit 1; fi


echo "Instalando las dependencias necesarias"
echo off
pip install -r requirements.txt


echo "Ejecutando el script de Alertas: CONTROL ACCESO, Madrid Digital y tamaño ficheros"
python3 ./src/alertas.py 


echo "Iniciando la aplicación web AppWebFinanzas"
python3 ./src/app.py


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."