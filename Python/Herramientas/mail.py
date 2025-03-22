import imaplib
import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders, message_from_bytes
import os



#  Lectura de mail de la bandeja de entrada
def Lectura_mail(user, password, etiqueta, busqueda, contar=False):
    # Conexión al servidor IMAP de Gmail 
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(user, password)

    mail.select(etiqueta) 
    _, data = mail.search(None, busqueda) 

    if contar:
        salida = len(data[0].split())
    else:
        mensajes = []
        # Itera sobre los IDs de los correos electrónicos encontrados 
        for num in data[0].split(): 
            _, data = mail.fetch(num, '(RFC822)')
        
            msg = message_from_bytes(data[0][1]) 
            print('Asunto:', msg['subject'], '\n   Remitente:', msg['from'])
            mensajes.append(msg)
        
        salida = mensajes
    
    # Cierra la conexión 
    mail.close()
    mail.logout()

    return salida



#  Configuración y envío del mail 
def Conexion(user, password, mensaje):
    context = ssl.create_default_context()
    smtp = "smtp.gmail.com"
    port = 465
    
    try:
        # Configurar el servidor SMTP y enviar el correo
        with smtplib.SMTP_SSL(smtp, port, context=context) as server:
            server.login(user, password)
            server.send_message(mensaje)
            print('Mail enviado correctamente.')
    except Exception as e:
        print(f"Error al enviar mail: {e}")
    

#  Envío mail sencillo (sin adjuntos)
def Envio_mail(user, password, asunto, mensaje, destinatario):
    msg = EmailMessage()
    msg['subject'] = asunto
    msg['to'] = destinatario
    msg.set_content(mensaje)

    Conexion(user, password, msg)


#  Envío mail con fichero adjunto
def Envio_mail_adjunto(user, password, asunto, mensaje, destinatario, archivo_adjunto):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(mensaje, 'plain'))

    # Adjuntar archivo
    with open(archivo_adjunto, 'rb') as adjunto:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(adjunto.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(archivo_adjunto)}')
        msg.attach(parte)

    Conexion(user, password, msg)




if __name__ == '__main__':
    from Herramientas.variables import USUARIO, PASSWORD, DESTINATARIO
    
    Envio_mail(USUARIO, PASSWORD , "ASUNTO: Prueba", "\n Mensaje", DESTINATARIO)
