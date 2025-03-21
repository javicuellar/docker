import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

#  Ignora los warnings que muestra los modelos
import warnings
warnings.filterwarnings('ignore')


#   Definir el límite de acceso, el scope = alcance, acceso a hojas de cálculo y drive
alcance =  ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']

Credenciales = ServiceAccountCredentials.from_json_keyfile_name('Credenciales.json', alcance)
cliente = gspread.authorize(Credenciales)

#  Trabajando con hoja copia -> **"Cartera limpia"**
#  https://docs.google.com/spreadsheets/d/1qGM6LUm9FO_KyVwv1-h9j9bS3c6uqfJi9-iH4qBJh1w/edit#gid=1100996300



def RecuperarCartera():
    #  Lectura de hoja google "Cartera limpia" => pestaña "Activos"
    hoja = cliente.open("Cartera limpia")
    activos = hoja.worksheet('Cartera')
    # lista_activos = activos.get_all_values()    # vuelca en Lista
    # print(lista_activos)

    # Recuperar todos los datos
    cartera = pd.DataFrame(activos.get_all_records())
    cartera = cartera[(cartera['Tipo']== 'Carteras') & (cartera['Entidad'] != 'TOTAL')]
    cartera = cartera[cartera['Fecha'] == cartera['Fecha'].max()]

    # Mostrar los datos
    tickers = cartera[cartera['Producto'] == 'Acciones']['Ticker'].tolist()
    # print(tickers)
    return tickers


def RecuperarCartera2():
    #  Lectura de hoja google "Cartera limpia" => pestaña "Activos"
    hoja = cliente.open("Cartera limpia")
    activos = hoja.worksheet('Cartera')
    # lista_activos = activos.get_all_values()    # vuelca en Lista
    # print(lista_activos)

    # Recuperar todos los datos
    cartera = pd.DataFrame(activos.get_all_records())
    # cartera = cartera[(cartera['Tipo']== 'Carteras') & (cartera['Entidad'] != 'TOTAL')]
    cartera = cartera[(cartera['Tipo']== 'Carteras')]
    cartera = cartera[cartera['Fecha'] == cartera['Fecha'].max()]

    cartera = cartera.drop(['Fecha','Tipo', 'Subtipo', 'Importe', 'Rent.', '% Rent', 'Saldo', '', 
                            'AñoMes', 'Abierta'], axis=1)
    cartera.rename(columns={'P. Venta/Ant.': 'P. Ant.'}, inplace=True)
    cartera = cartera[['Descripción', 'Entidad', 'Producto', 'Num.', 'Precio', 'P. Ant.',
       'Tipo Act.', 'Ticker']]
    return cartera




if __name__ == '__main__':
    datos = RecuperarCartera2()
    print(datos)