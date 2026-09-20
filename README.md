# docker

Repositorio con las definiciones **docker-compose** de los servicios desplegados en el NAS Synology. Cada proyecto vive en su propia carpeta con un `docker-compose.yaml` independiente, para poder desplegarlo y mantenerlo por separado desde Container Manager / Portainer.

## Estructura del repositorio

```
docker/
├── synology.env              # Variables comunes del NAS (PUID, PGID, TZ, idioma)
├── multimedia/                # Servicios de gestión y consumo multimedia
│   ├── calibreweb/
│   └── calibreweb-automated/
└── utilidades/                 # Herramientas de soporte y utilidades generales
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
