# docker

Repositorio con las definiciones **docker-compose** de los servicios desplegados en el NAS Synology. Cada proyecto vive en su propia carpeta con un `docker-compose.yaml` independiente, para poder desplegarlo y mantenerlo por separado desde Container Manager / Portainer.

## Estructura del repositorio

```
docker/
├── synology.env                    # Variables comunes del NAS (PUID, PGID, TZ, idioma)
├── multimedia/                     # Servicios de gestión y consumo multimedia
│   ├── calibreweb/
│   ├── calibreweb-automated/
│   ├── jellyfin/
│   ├── multimedia_suite/           # Stack *arr completo (descargas, indexadores, streaming)
│   ├── plex/
│   └── tinymediamanager/
└── utilidades/                     # Herramientas de soporte y utilidades generales
    ├── duplicati/
    └── nametag/
```

Cada carpeta de proyecto sigue el mismo patrón:

- `docker-compose.yaml`: definición del/los servicio(s).
- `*.env` (no versionado): variables privadas propias del proyecto, referenciadas desde el `docker-compose.yaml` junto con `synology.env`.
- Carpetas de datos (`config`, `libreria`, `watch`, `db`, `backups`, etc.): volúmenes persistentes, no versionados.

> Los ficheros `.env`, certificados (`*.pem`) y credenciales (`*.json`) están excluidos del control de versiones (ver [.gitignore](.gitignore)). Deben crearse manualmente en el NAS antes de levantar cada stack.

## Inventario de proyectos

| Proyecto | Categoría | Imagen | Puerto | Descripción |
|---|---|---|---|---|
| [calibreweb](multimedia/calibreweb/) | Multimedia | `linuxserver/calibre-web` | 8083 | Servidor web de biblioteca de libros Calibre. |
| [calibreweb-automated](multimedia/calibreweb-automated/) | Multimedia | `crocodilestick/calibre-web-automated` | 8083 | Calibre-Web con ingesta automática: los libros depositados en `watch` se procesan y añaden solos a la biblioteca. |
| [jellyfin](multimedia/jellyfin/) | Multimedia | `linuxserver/jellyfin` | 8096 | Servidor multimedia libre para películas, series y música, con transcodificación por hardware Intel Quick Sync. |
| [multimedia_suite](multimedia/multimedia_suite/) | Multimedia | `linuxserver/qbittorrent` + `prowlarr` + `jackett` + `sonarr` + `radarr` + `jellyfin` + `plex` | 8080, 9696, 9117, 8989, 7878, 8096, 32400 (host) | Suite multimedia completa: descarga por torrent, indexadores, gestión automática de películas/series y servidores de streaming. |
| [plex](multimedia/plex/) | Multimedia | `linuxserver/plex` | 32400 (host) | Servidor multimedia Plex sobre la videoteca del NAS, con transcodificación por hardware. |
| [tinymediamanager](multimedia/tinymediamanager/) | Multimedia | `romancin/tinymediamanager:latest-v4` | 5800 (web), 5900 (VNC) | Gestor de metadatos (NFO, carátulas, fanart) para películas y series. |
| [duplicati](utilidades/duplicati/) | Utilidades | `linuxserver/duplicati` | 8200 | Copias de seguridad programadas de las carpetas indicadas en `source`. |
| [nametag](utilidades/nametag/) | Utilidades | `mattogodoy/nametag` + `postgres` + `redis` | 3753 | Aplicación de etiquetado de contactos, con base de datos PostgreSQL, caché Redis y tarea cron de recordatorios diarios. |

## Detalle de proyectos

### 📚 [multimedia/calibreweb](multimedia/calibreweb/)
Instancia clásica de Calibre-Web sobre la biblioteca existente en `/volume2/libros`. Incluye el mod `universal-calibre` para conversión de formatos.

### 📚 [multimedia/calibreweb-automated](multimedia/calibreweb-automated/)
Evolución de Calibre-Web que añade ingesta automática de libros: cualquier fichero copiado en `watch/` se procesa y se mueve a `libreria/` según la configuración de CWA. Sustituye progresivamente a `calibreweb`.

- `config/`: configuración y ajustes de usuario de CWA.
- `watch/`: carpeta de entrada (ingest); los ficheros se eliminan tras procesarse.
- `libreria/`: biblioteca Calibre resultante.
- `plugins/`: plugins de Calibre opcionales.

### 🎬 [multimedia/jellyfin](multimedia/jellyfin/)
Servidor multimedia de código abierto. Expone la interfaz web en el puerto 8096 y usa la GPU Intel (`/dev/dri`) para transcodificación por hardware, con el mod `jellyfin-opencl-intel` para tone mapping vía OpenCL.

- `config/`: configuración, metadatos y base de datos de Jellyfin.
- Bibliotecas montadas en `/data`:
  - `/volume2/video/peliculas` → `/data/peliculas`
  - `/volume2/video/series` → `/data/series`
  - `/volume2/music` → `/data/musica`
- `pruebas/`: variantes del `docker-compose.yaml` usadas durante las pruebas de configuración.

### 🧩 [multimedia/multimedia_suite](multimedia/multimedia_suite/)
Stack completo de automatización multimedia en un único `docker-compose.yaml`. Las rutas base se parametrizan en el `.env` del proyecto:

- `ARRPATH`: ruta base de configuración y bibliotecas de la suite.
- `DESCARGAS`: ruta base donde se crea la carpeta compartida `descargas_suite` (montada en `/downloads` en todos los servicios de descarga y gestión).

| Servicio | Contenedor | Puerto | Función |
|---|---|---|---|
| qBittorrent | `qbittorrent` | 8080 (web), 6881 TCP/UDP | Cliente torrent. |
| Prowlarr | `prowlarr` | 9696 | Gestor centralizado de indexadores para Sonarr/Radarr. |
| Jackett | `jackett` | 9117 | Proxy de indexadores (alternativa/complemento a Prowlarr). |
| Sonarr | `sonarr` | 8989 | Gestión y descarga automática de series → `sonarr/series`. |
| Radarr | `radarr` | 7878 | Gestión y descarga automática de películas → `radarr/peliculas`. |
| Jellyfin | `jellyfin` | 8096, 7359/udp | Streaming de las bibliotecas de la suite (`/data/movies`, `/data/tvshows`) y de la videoteca/música del NAS (`/data/peliculas`, `/data/series`, `/data/musica`). |
| Plex | `plex_suite` | 32400 (host) | Streaming de las bibliotecas de Sonarr/Radarr, en `network_mode: host`. |

- Cada servicio guarda su configuración en `<servicio>/config/`; Prowlarr, Sonarr y Radarr además hacen copias en `<servicio>/backup/`.
- El puerto DLNA 1900/udp de Jellyfin está comentado por estar ya en uso en el NAS.
- ⚠️ Los puertos 8096 y 32400 coinciden con los de los proyectos independientes [jellyfin](multimedia/jellyfin/) y [plex](multimedia/plex/): no deben ejecutarse a la vez que la suite.
- Para reclamar Plex automáticamente, descomentar `PLEX_CLAIM` con un token válido.

### 🎞️ [multimedia/plex](multimedia/plex/)
Servidor multimedia Plex. Funciona en `network_mode: host` (interfaz web en `http://<nas>:32400/web`) para facilitar el descubrimiento DLNA/GDM en la red local, y usa `/dev/dri` para transcodificación por hardware (requiere Plex Pass).

- `config/`: configuración y base de datos de Plex.
- `/volume2/video` → `/movies`: videoteca del NAS.
- `docker-compose (anterior).yaml`: versión previa del compose, conservada como referencia.

### 🏷️ [multimedia/tinymediamanager](multimedia/tinymediamanager/)
tinyMediaManager v4 para organizar y completar metadatos (ficheros NFO, carátulas, fanart, renombrado) de películas y series. Es una aplicación de escritorio servida por navegador (`http://<nas>:5800`) o por cliente VNC (puerto 5900).

- `config/`: configuración y base de datos de tinyMediaManager.
- `/volume2/video/peliculas/clara` → `/media`: carpeta de medios gestionada.
- `.env`: `USER_ID` y `GROUP_ID` con los que se ejecuta la aplicación.

### 💾 [utilidades/duplicati](utilidades/duplicati/)
Herramienta de copias de seguridad cifradas y programadas.

- `source/`: origen de los datos a respaldar.
- `backups/`: destino local de las copias.
- `config/`: configuración de trabajos de backup.

### 🏷️ [utilidades/nametag](utilidades/nametag/)
Stack de 4 servicios:

- `db`: PostgreSQL 18 con healthcheck.
- `redis`: caché/cola con contraseña.
- `nametag`: aplicación principal (puerto 3753 → 3000).
- `cron`: lanza diariamente a las 8:00 una llamada al endpoint de recordatorios de la app.

## Requisitos previos

1. Synology NAS con Docker / Container Manager.
2. Fichero [`synology.env`](synology.env) en la raíz con `PUID`, `PGID`, `TZ`, `LANGUAGE` y `LANG`.
3. Un fichero `.env` privado por proyecto (referenciado en cada `docker-compose.yaml`) con las credenciales y variables específicas del servicio.

## Despliegue

Desde la carpeta del proyecto deseado:

```bash
docker compose up -d
```
