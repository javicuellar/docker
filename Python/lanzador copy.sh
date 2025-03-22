#!/bin/bash

#  Script multifuncional para ejecutar desde el contenedor cualquier proyecto

#  Terminal python para pruebas
terminal_python() {
  echo "Terminal python"
  ./bin/bash
}


#  Ejecución proyecto AppWeb + Alertas
ejecutar_appweb() {
  echo "Ejecutando Proyecto AppWeb + Alertas en python Flask"
  cd ./python/AppWeb_alertas
  pip install -r requirements.txt
  ./ejecutar.sh
}


echo "Ejecución del Terminal python por defecto."
terminal_python

#  Menú opciones multiprocesos a ejecutar
echo "Menú de procesos a ejecutar, selecciona una opción:"
echo "  1 - Terminal Python"
echo "  2 - prueba"
echo "  3 - Fin"
read opcion


if [ "$opcion" == "1" ]; then
  terminal_python

elif [ "$opcion" == "2" ]; then
  cd ./prueba
  ./ejecutar.sh

elif [ "$opcion" == "3" ]; then
  echo "Opción 2 no configurada."

else
  echo "Opción inválida."

fi

echo "Proceso completado."