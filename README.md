# Proyectos en E:\

Índice de los proyectos y recursos de esta unidad. La mayoría están pensados para ejecutarse en Docker sobre el NAS Synology.

| Carpeta | Contenido |
|---|---|
| [docker/](docker/) | Definiciones `docker-compose` de los servicios del NAS |
| [python/](python/) | Proyectos y apps web en Python |
| [python_bd/](python_bd/) | Bases de datos SQLite compartidas |
| [python_config/](python_config/) | Credenciales, certificados SSL y `config.env` (**no compartir**) |
| [telegram/](telegram/) | Bot de Telegram para torrents |
| [Leeme Docker.md](Leeme%20Docker.md) | Comandos básicos de Docker en el NAS (SSH, crear contenedores) |
| [NAS Docker.md](NAS%20Docker.md) | Enlaces a los proyectos publicados en GitHub |

---

## 📈 Alertas de bolsa por Telegram

**Proyecto: [python/11_Monitor_alertas/](python/11_Monitor_alertas/)**

Comprueba periódicamente el precio de acciones y ETFs (con `yfinance`) y avisa por **Telegram** y/o **email** cuando un valor sube o baja más del porcentaje configurado respecto al cierre del día hábil anterior.

- Panel de administración Streamlit en `http://localhost:8501`: símbolos y umbrales, planificador (intervalo, horario, días), configuración de Telegram (token y chat ID), email e historial de alertas.
- Configuración e historial guardados en SQLite (`data/monitor.db`).
- Arranque: `python monitor_acciones/arrancar.py`. Opciones: `--solo-admin`, `--solo-monitor`, `--una-vez` (para cron) y `--puerto`.
- La lógica de Telegram está en `monitor_acciones/stock_monitor/notifications.py`.

---

## 🐳 docker/

Cada servicio tiene su carpeta con su `docker-compose.yaml` y su `.env`. `synology.env` guarda las variables comunes (PUID, PGID, TZ). Más detalles en [docker/README.md](docker/README.md).

### multimedia/
| Servicio | Descripción |
|---|---|
| calibreweb / calibreweb-automated | Biblioteca de libros electrónicos |
| jellyfin / plex | Servidores multimedia |
| multimedia_suite | Stack completo: qBittorrent, Jackett, Prowlarr, Radarr, Sonarr, Jellyfin, Plex |
| tinymediamanager | Gestión de metadatos de películas y series |

### telegram/
| Bot | Descripción |
|---|---|
| controller-bot | Control de contenedores Docker desde Telegram (`dgongut/docker-controller-bot`) |
| torrent-controller-bot | Control de descargas torrent (`dgongut/torrent-controller-bot`) |
| dropbot | Descarga de archivos enviados al bot (`dgongut/dropbot`) |
| intrubot | Avisos de intrusión/dispositivos en la red (`dgongut/intrubot`) |
| cumplebot | Recordatorio de cumpleaños y precio de Bitcoin |
| torrentbot | Bot.Torrent v4 en Python |
| prueba | Imagen propia de pruebas |

### utilidades/
| Servicio | Descripción |
|---|---|
| MariaDB | Notas de la base de datos MariaDB |
| Selenium-Chrome | Navegador Chrome remoto para scraping |
| descargas | rutorrent y transmission |
| duplicati | Copias de seguridad |
| metube | Descarga de vídeos de YouTube |
| nametag | Nametag con base de datos y Redis |
| navegadores | Firefox y Opera en contenedor |
| pihole | Bloqueo de publicidad por DNS |
| wireguard | VPN |

### ejemplos/
Plantillas de `Dockerfile` y `docker-compose` (Python, redes, etc.).

---

## 🐍 python/

Entorno común: `crear_entorno.bat`, `activar_entorno.bat`, `instalar_requirements.bat`, `lanzador.sh`, `Dockerfile` y `docker-compose.yaml`. La configuración y las credenciales están en `config/` y `config.env`.

### Proyectos numerados
| Carpeta | Descripción |
|---|---|
| 01_appweb_flask_SQLite | Primera app Flask con login y SQLite (base de AppWeb_alertas) |
| 01_appweb_flask_SQLite_HTTPS | Igual que la anterior, servida por HTTPS |
| 02_appweb_flask_upload_file | Flask con log rotativo y subida de ficheros desde PC/móvil |
| 03_selenium-scrapper | Scraping con Selenium + Chrome en contenedores (alerta de esquí) |
| 04_App_tienda_videojuegos | Tienda de videojuegos en Flask (de josedom24) |
| 05_appweb_flet | Ejemplo con Flet (no funciona: falta `flet_desktop`) |
| 06_AppWeb_alertas | App Flask de cartera de activos con alertas por **email** (Google Sheets, Madrid Digital, ficheros) |
| 08_appweb_streamlit | Ejemplo mínimo de Streamlit con HTTPS |
| 09_App_Finanzas | App Streamlit de finanzas: movimientos, cartera y resumen del IRPF |
| 10_find_video_duplicates | Buscador de vídeos duplicados (Streamlit) |
| **11_Monitor_alertas** | **Monitor de acciones con alertas por Telegram/email** (ver arriba) |
| 12-variables-entorno | Ejemplo de configuración mediante variables de entorno |

### Proyectos/
| Carpeta | Descripción |
|---|---|
| 07_Appweb_contactos | App web de gestión de contactos con alertas |
| 12_pocha | La Pocha: contador de puntos del juego de cartas (Streamlit, SQLite, PDF) |
| 17-contactos | Gestión de contactos en Flask (eventos, relaciones, etiquetas, importación de Google Contacts) |
| 19-panel-javi | Panel estático con Google Calendar y TickTick que se regenera cada hora (generador + nginx) |
| 21-gym | Registro de sesiones de gimnasio (Flask + SQLite) |
| 22-bitacora | Enlaces e información guardados desde el correo, clasificados por temas |

### Otras carpetas
| Carpeta | Descripción |
|---|---|
| Proyectos (ant) | Versiones anteriores de proyectos (Finanzas, Alertas, Nametag, CineStream…) |
| Herramientas | Módulos comunes: variables, mail (Gmail), scraping, sheet (Google Sheets), BD SQLite/MySQL |
| Python | Repositorio de formación: cursos, Data Science, ejemplos y librerías |
| Documentos_Ayuda | PDFs, libros y tutoriales (Docker, Git, Markdown, Python, VS Code) |
| Tutorial_git | Tutorial de Git con ejemplos |
| Repositorios_Clonados | Repositorios de terceros |
| bd | Bases de datos (SQLite, DES) y logs |
| venv | Entorno virtual de Python |

---

## 📲 telegram/

- **bot-torrent**: `Bot.torrent.v4.py` + `config.ini`. Bot de Telegram para gestionar torrents (es la misma versión que `docker/telegram/torrentbot`).

---

> ⚠️ `python_config/`, `python/config/` y otras carpetas contienen credenciales (`Credenciales.json`, `*.pem`, `*.env`). No las subas a repositorios públicos.
