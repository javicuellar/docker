import os
from app.app import app as aplicacion






if __name__ == "__main__":
    if os.name == 'nt':
        aplicacion.run(port=5010)
    else:
        # Conexión segura https para el NAS
        aplicacion.run(ssl_context=('cert.pem', 'privkey.pem'),host="192.168.1.41", port=5010, debug=True)
