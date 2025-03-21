import gspread, os
from oauth2client.service_account import ServiceAccountCredentials   # para usar credenciales



#   Definir el límite de acceso, el scope = alcance, acceso a hojas de cálculo y drive
alcance =  ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']

if os.name == 'nt':
    Credenciales = ServiceAccountCredentials.from_json_keyfile_name('\\Python\\Credenciales.json', alcance)
else:
    Credenciales = ServiceAccountCredentials.from_json_keyfile_name('./Credenciales.json', alcance)

cliente = gspread.authorize(Credenciales)




#  Abre la hoja de cálculo y actualiza los datos
def Actualizar_Hoja(nombre_hoja, datafame):
    hoja = cliente.open(nombre_hoja).sheet1
    hoja.clear()
    cabecera = datafame.columns.values.tolist()
    datos = datafame.values.tolist()
    hoja.update([cabecera] + datos) 
