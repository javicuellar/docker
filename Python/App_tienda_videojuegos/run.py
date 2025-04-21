# import sys
# sys.path.insert(0, '/var/www/html/tienda_videojuegos')

from aplicacion.app import app as application


if __name__ == "__main__":
    # application.run(port=5004)

# Conexión segura https para el NAS
    application.run(ssl_context=('cert.pem', 'privkey.pem'),host="192.168.1.41", port=5010, debug=True)
    