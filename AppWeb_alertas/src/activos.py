import yfinance as yf



class FinanzasApp:
    def __init__(self, datos):
        self.activos = datos
        self.stocks = {}
        self.descarga()


    def descarga(self):
        if len(self.activos['activos']) != 0:
            print('DESCARGANDO INFORMACIÓN DE ACTIVOS')
            for ticker in self.activos['activos']:
                self.stocks[ticker] = yf.Ticker(ticker)
                print(f'Información de {ticker} descargada')
            print('DESCARGA COMPLETA\n')
        else:
            print('No hay tickers para descargar')


    def informe_ultimo_valor(self):
        salida = []
        for stock in self.stocks.keys():
            ultimo_valor = self.stocks[stock].history(period='1d')['Close'][0]
            # print(f'{stock}: $ {ultimo_valor}')
            salida.append([stock, round(ultimo_valor,2)])
        return salida


    def informe_cambio_ultimo_periodo(self):
        salida = []
        for stock in self.stocks.keys():
            valores = self.stocks[stock].history(period='1mo')['Close'].values
            dif = round(valores[-1] - valores[0],2)
            # print(f'{stock}: $ {valores[0]} -> $ {valores[-1]} Dif.: {dif}   % Dif.:  {(dif / valores[0]):.2%}')
            salida.append([stock, round(valores[-1],2), round(valores[0],2), dif, round((dif / valores[0])*100,2)])
        return salida