import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from Herramientas.sheet import Actualizar_Hoja




def Alerta_viaje_esqui(terminos_busqueda):
  print("Inicio del programa: esperando a que se inicie contenedor selenium_chrome")
  sleep(20)   # Esperar a que se inicie el servidor de selenium_chrome

  chrome_options = Options()
  chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebkit/537.36 (KHTML, like Gecko) "
                              "Chrome/91.0.4472.77 Safari/537.36")
  
  service = Service(ChromeDriverManager().install())
  sleep(5)

  try:
    browser = webdriver.Remote("http://192.168.1.41:4444", options=chrome_options)
  
  except Exception as e:
    print(f"Error al conectar con servidor selenium: {e}")
    exit()

  browser.get("https://duckduckgo.com")
  
  # Para cada término, realizamos la búsqueda y extraemos los resultados
  resultados_globales = []
  for termino in terminos_busqueda:
    # Encontrar termino en caja de búsqueda
    caja_busqueda = browser.find_element(By.NAME, "q")
    caja_busqueda.send_keys(termino)
    caja_busqueda.send_keys(Keys.RETURN)

    # Esperar a que se carguen los resultados
    sleep(3)

    # Extraer títulos y enlaces de los resultados
    resultados = []
    resultados_termino = []
    while len(resultados) < 30:
      resultados = browser.find_elements(By.CSS_SELECTOR, "h2 a")

      try:
        caja_mas_resultados = browser.find_element(By.ID, "more-results")
        caja_mas_resultados.send_keys(Keys.RETURN)

        sleep(3)
      except Exception:
        break
    
    for resultado in resultados:
      try:
        titulo = resultado.text                     # Texto del enlace (título del resultado)
        enlace = resultado.get_attribute("href")    # Enlace del resultado
        if titulo and enlace:
          resultados_termino.append({
            "Búsqueda": termino,
            "Título": titulo,
            "Enlace": enlace
            })
          # print(f"Resultado: {titulo} - {enlace}")
      except Exception:
        print("Error al extraer resultados")

    resultados_globales.extend(resultados_termino)


  # Guardar resultados en archivo
  df = pd.DataFrame(resultados_termino)
    
  Actualizar_Hoja('Alertas Esqui', df)


  browser.quit()

  print("Fin del programa")





if __name__ == "__main__":
    terminos = [
        "viaje esqui ayuntamiento",
        "viaje esqui ayuntamiento 2025",
        ]
    
    Alerta_viaje_esqui(terminos)
    
    print("Búsqueda finalizada. Resultados guardados en 'Alertas Esqui'")
