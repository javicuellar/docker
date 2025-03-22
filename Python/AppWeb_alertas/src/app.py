from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

#  Obtención de variables de entorno
import os
from dotenv import load_dotenv

load_dotenv('config.env')
secret_key = os.getenv("SECRET_KEY")
database = os.getenv("SQLALCHEMY_DATABASE_URI")
#  ------------------------------------------------


#  Módulo de finanzas para recuperar información de activos
from activos import FinanzasApp
from sheet import RecuperarCartera, RecuperarCartera2
#   --------------------------------------------------------




app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = database


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)




@app.before_request
def before_request():
    if request.scheme != 'https':
        return redirect(request.url.replace('http://', 'https://'))


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = Usuario.query.filter_by(username=username, password=password).first()
        if usuario:
            login_user(usuario)
            if username == 'javi':
                return redirect(url_for('cartera_completa'))
            else:
                return redirect(url_for('usuarios'))
        else:
            flash('Credenciales incorrectas.')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nuevo_usuario = Usuario(username=username, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario registrado exitosamente. Puedes iniciar sesión.')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/usuarios')
@login_required
def usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.username = request.form['username']
        usuario.password = request.form['password']
        db.session.commit()
        flash('Usuario actualizado exitosamente.')
        return redirect(url_for('usuarios'))
    return render_template('edit_user.html', usuario=usuario)


@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado exitosamente.')
    return redirect(url_for('usuarios'))


@app.route('/activos')
@login_required
def activos():
    data = {
        'activos': ['MSFT', 'NVDA', 'AAPL'],
        'objetivos': {
            'MSFT': [350, 500],
            'NVDA': [350, 500],
            'AAPL': [350, 500]
                    }
        }
    data['activos'] = RecuperarCartera()

    app = FinanzasApp(data)
    app.activos['activos'] 
    activos = app.informe_cambio_ultimo_periodo()
    return render_template('activos.html', activos=activos)


@app.route('/cartera_completa')
@login_required
def cartera_completa():
    df = RecuperarCartera2()
    
    acciones = df[(df['Producto']== 'Acciones')]
    acciones_html = acciones.to_html(classes='table table-striped', index=False)
    
    etfs = df[(df['Producto']== 'ETF')]
    etfs_html = etfs.to_html(classes='table table-striped', index=False)
    
    pensiones = df[(df['Producto']== 'P. Pensiones')]
    pensiones_html = pensiones.to_html(classes='table table-striped', index=False)
    
    cuentas = df[(df['Producto']== 'Cuenta')]
    cuentas_html = cuentas.to_html(classes='table table-striped', index=False)
    
    return render_template('cartera_completa.html', acciones=acciones_html, etfs=etfs_html, pensiones=pensiones_html,
                                            cuentas=cuentas_html)


@app.route('/cartera')
@login_required
def cartera():
    df = RecuperarCartera2()
    df = df[(df['Producto'] != 'TOTAL')]
    
    total = df.groupby('Producto').agg({'Precio': 'sum', 'P. Ant.': 'sum'}).reset_index()
    total_html = total.to_html(classes='table table-striped', index=False)
    return render_template('cartera.html', total=total_html)



@app.route('/dataframe')
def dataframe():
    data = {
        'Nombre': ['Google', 'Facebook', 'Twitter'],
        'Enlace': ['https://www.google.com', 'https://www.facebook.com', 'https://www.twitter.com']
            }
    
    import pandas as pd

    df = pd.DataFrame(data)

    # Convertir el DataFrame a una lista de diccionarios
    data = df.to_dict(orient='records')
    print(data)
    return render_template('dataframe.html', data=data)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




if __name__ == '__main__':
    with app.app_context():
        db.create_all()         # Crea la base de datos

    # En el navegador -> http://javicu.synology.me:5010/login  o  http://192.168.1.41:5010/login
    # app.run(host="192.168.1.41", port=5010, debug=True)
    # no poner como host "javicu.synology.me", ni localhost, no han funcionado

    # Conexión segura https para el NAS
    app.run(ssl_context=('cert.pem', 'privkey.pem'),host="192.168.1.41", port=5010, debug=True)
    
    # Línea para ejecutar en PC
    # app.run(ssl_context=('cert.pem', 'privkey.pem'),host='localhost', port=5015, debug=True)