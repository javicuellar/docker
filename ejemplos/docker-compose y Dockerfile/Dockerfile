FROM ubuntu:22.04

WORKDIR /app

# Copiar código fuente de la aplicación
COPY ./src /app

# Instalar dependencias del sistema, descargar código e instalar dependencias Python en una sola capa
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip && \
    # Instalar dependencias de Python antes de limpiar pip
    pip3 install --no-cache-dir -r /app/requirements.txt
