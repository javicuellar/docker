from Herramientas.variables import USUARIO, PASSWORD, USUARIO_JAVI, PASSWORD_JAVI
from alerta_CONTROL import Alerta_CONTROL
from alerta_MD import Alerta_MD
# from alerta_ficheros import Alerta_Ficheros               # Genera fichero excel
from alerta_ficheros_sheet import Alerta_Ficheros_sheet     # Actualiza hoja de cálculo




#     Analizamos las alertas:

#  Alerta CONTROL ACCESO, si no borro los correos de CONTROL ACCESO se activa la alerta
Alerta_CONTROL(USUARIO, PASSWORD, USUARIO_JAVI, PASSWORD_JAVI)

#  Alerta puestos en Madrid Digital
Alerta_MD(USUARIO, PASSWORD, USUARIO_JAVI)


#  Analizamos ficheros en DIRECTORIO mayores de T_MINIMO 
T_MINIMO = 5 * 1024 * 1024 * 1024      # GB en bytes (1024 bytes x 1024 Mb x 1024 Gb)

# Para Windows añadimos path a librerías python, para añadir librerías mías de Herramientas
import sys, os
if os.name == 'nt':
    sys.path.append(os.path.join(os.path.dirname(__file__), '\\Python'))
    DIRECTORIO = 'D:\\'
else:
    DIRECTORIO = '/video'

Alerta_Ficheros_sheet(DIRECTORIO, T_MINIMO)