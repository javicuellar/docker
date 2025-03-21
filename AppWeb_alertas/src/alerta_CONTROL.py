from Herramientas.mail      import Envio_mail, Lectura_mail



#  Docuementar la alerta

def Alerta_CONTROL(usuario, password, usuario_javi, password_javi):
    #  Recuperamos el número de correos con asunto CONTROL ACCESO
    num = Lectura_mail(usuario_javi, password_javi, 'inbox', '(SUBJECT "CONTROL ACCESO")', contar=True)
    
    if num > 4:
        alerta = 'ALERTA CONTROL ACCESO - Demasiados correos'
        mensaje = f"Se han recibido {num} avisos. \nSE TOMARÁN MEDIDAS"
        Envio_mail(usuario, password , alerta, mensaje, usuario_javi)
    else:
        asunto = 'CONTROL ACCESO - Mail de control automático'
        mensaje = f"Aviso de control de acceso num. {num + 1}."
        Envio_mail(usuario, password , asunto, mensaje, usuario_javi)




if __name__ == '__main__':
    from Herramientas.variables import USUARIO, PASSWORD, USUARIO_JAVI, PASSWORD_JAVI
    
    Alerta_CONTROL(USUARIO, PASSWORD, USUARIO_JAVI, PASSWORD_JAVI)