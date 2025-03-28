from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep



print("Inicio del programa: esperando 5 minutos")
sleep(20)

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebkit/537.36 (KHTML, like Gecko) "
                            "Chrome/91.0.4472.77 Safari/537.36")

service = Service(ChromeDriverManager().install())

try:
  browser = webdriver.Remote("http://192.168.1.41:4444", options=chrome_options)
  
  browser.get("https://medium.com")
  print("Titulo de la pagina: ", browser.title)
  browser.quit()

except Exception as e:
  print(f"Error al conectar con servidor selenium: {e}")
  exit()

print("Fin del programa")
