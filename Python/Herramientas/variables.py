import os
from dotenv import load_dotenv



if os.name == 'nt':
    load_dotenv('\\Python\\config.env')
else:
    load_dotenv('./config.env')

USUARIO = os.getenv("USER_MAIL")
PASSWORD = os.getenv("PASSWORD_MAIL")
DESTINATARIO = os.getenv("DESTINATARIO_MAIL")
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
USUARIO_JAVI = os.getenv("USER_JAVI")
PASSWORD_JAVI = os.getenv("PASSWORD_JAVI")