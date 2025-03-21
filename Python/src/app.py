from flask import Flask, render_template, request, redirect, url_for, session
import os
import datetime
import logging


# Configura el Registro
#  - configura un registrador (logger) para tu aplicación. 
#  Puedes configurar diferentes niveles de registro (DEBUG, INFO, WARNING, ERROR, CRITICAL) para controlar qué tipo de mensajes
#  se registran.
# Configura el registrador
logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')


# Configura el Registro con Rotación de Archivos
#   Puedes configurar el registrador para rotar los archivos de registro automáticamente cuando alcancen un tamaño determinado o
#   después de un cierto período de tiempo. Esto te ayudará a evitar que los archivos de registro se vuelvan demasiado grandes.
import logging.handlers
# Configura el registrador con rotación de archivos
handler = logging.handlers.RotatingFileHandler('app.log', maxBytes=1024 * 1024 * 5, backupCount=5, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)


# Ejemplo de registro de un mensaje de depuración
logging.debug('Inicio de la aplicación')

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# Simulación de usuarios
usuarios = {'admin': '1234'}


# Lista de contactos de muestra
contactos = [
    {'nombre': 'Juan', 'apellidos': 'Pérez', 'telefono': '1234567890'},
    {'nombre': 'Ana', 'apellidos': 'García', 'telefono': '9876543210'},
    {'nombre': 'Pedro', 'apellidos': 'Rodríguez', 'telefono': '5551234567'}
]



@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    logging.info('Intento de inicio de sesión: Usuario=%s', usuario)
    if usuario in usuarios and usuarios[usuario] == contraseña:
        session['usuario'] = usuario
        logging.info('Inicio de sesión exitoso: Usuario=%s', usuario)
        return redirect(url_for('menu'))
    else:
        logging.warning('Inicio de sesión fallido: Usuario=%s', usuario)
        return 'Usuario o contraseña incorrectos'


@app.route('/menu')
def menu():
    if 'usuario' not in session:
        return redirect(url_for('home'))
    return render_template('menu.html')


@app.route('/archivos', methods=['POST'])
def mostrar_archivos():
    directorio = request.form['directorio']
    archivos_recientes = []
    una_semana = datetime.timedelta(days=7)
    ahora = datetime.datetime.now()
    limite_tiempo = ahora - una_semana

    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            tiempo_modificacion = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_completa))
            if tiempo_modificacion > limite_tiempo:
                archivos_recientes.append((ruta_completa, tiempo_modificacion.strftime('%Y-%m-%d %H:%M:%S')))
    return render_template('menu.html', archivos=archivos_recientes)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'usuario' not in session:
        return redirect(url_for('home'))
    
    if 'file' not in request.files:
        return 'No se ha seleccionado ningún archivo'
    
    file = request.files['file']
    if file.filename == '':
        # Ejemplo de registro de un mensaje de advertencia
        logging.warning('No ha seleccionado ningún archivo: %s', file.filename)

        return 'No se ha seleccionado ningún archivo'

    # Ejemplo de registro de un mensaje de error
    try:
        # Código que puede generar un error
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))     # este código no puede fallar, pero estoy probando log
    except Exception as e:
        logging.error('Error: %s', e)
    return redirect(url_for('menu'))


@app.route('/contactos')
def contactos_view():
    if 'usuario' not in session:
        return redirect(url_for('home'))
    return render_template('contactos.html', contactos=contactos)


@app.route('/seleccionar_contacto', methods=['POST'])
def seleccionar_contacto():
    if 'usuario' not in session:
        return redirect(url_for('home'))
    nombre_seleccionado = request.form.get('nombre')
    contacto_seleccionado = next((c for c in contactos if c['nombre'] == nombre_seleccionado), None)

    if contacto_seleccionado:
        return f"Has seleccionado: {contacto_seleccionado['nombre']} {contacto_seleccionado['apellidos']}, Teléfono: {contacto_seleccionado['telefono']}"
    else:
        return "Contacto no encontrado"



@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(port=5010, debug=True)
    # app.run(host="192.168.1.41", port=5010, debug=True)