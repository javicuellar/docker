# -*- coding: utf-8 -*-
print("\033c")
LICENCIA = """
BOT.Torrent - 4.0 :
Este programa es software GRATUITO: puedes redistribuirlo y/o modificar
bajo los términos de la Licencia Pública General GNU publicada por
la Free Software Foundation, ya sea la versión 3 de la Licencia, o
(a su elección) cualquier versión posterior.

Este programa se distribuye con la esperanza de que sea útil,
pero SIN NINGUNA GARANTÍA, ni RESPONSABILIDAD; sin siquiera la garantía implícita de
COMERCIABILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Ver el
Licencia pública general GNU para obtener más detalles <https://www.gnu.org/licenses/>.

El USUARIO de este programa, es el UNICO RESPONSABLE, de que el USO del mismo, 
se limita, al estricto cumplimiento, de cualquier LEY, aplicable.
"""
"""
# DekkaR - 2024
"""
import os
if os.path.exists("bot_4" + ".session"): os.remove("bot_4" + ".session")

from time import sleep, time
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Variables globales
folder_name = ""
last_forward_time = 0

###
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
api_id = int(config['bot']['api_id'])
api_hash = config['bot']['api_hash']
bot_token = config['bot']['bot_token']
mensaje_inicio = config['bot'].get('mensaje_inicio', 'Bot.Torrent.v4 en linea…')
directorio_torrent = config['bot']['directorio_torrent']
directorio_multimedia = config['bot']['directorio_multimedia']
usuario_id = int(config['bot']['usuario_id'])

###
import asyncio
import uvloop
from pyrogram import Client, filters

uvloop.install()
app = Client("bot_4", api_id = api_id, api_hash = api_hash, bot_token = bot_token)
with app:
    print("BOT.Torrent 4.0 : ", dt_string)
    app.send_message(usuario_id, mensaje_inicio)

###
# Arranque
@app.on_message(filters.command("start"))
async def send_welcome(client, message):
    await message.reply_text(mensaje_inicio)
    sleep(3)
    await message.delete()

# Licencia
@app.on_message(filters.command("licencia"))
async def send_licencia(client, message):
    await message.reply_text(LICENCIA)
    sleep(3)
    await message.delete()

# Audio
@app.on_message(filters.audio)
async def download_audio(client, message):
    global folder_name, last_forward_time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # Crear un directorio para multimedia basado en el nombre del archivo
    if not folder_name or (time() - last_forward_time > 30):
        folder_name = f"Audio_{now.minute}_{message.audio.title}"
        print(dt_string + " Carpeta: " + folder_name)
        last_forward_time = time()
        
    full_path = os.path.join(directorio_multimedia, folder_name)
    download_path = os.path.join(full_path, message.audio.file_name)
    # Si ha pasado demasiado tiempo desde el último mensaje reenviado, resetear
    if time() - last_forward_time > 30: folder_name = ""
    # Descargar el archivo
    print(" > " + message.audio.file_name)
    await message.reply_text(" > " + message.audio.file_name)
    await asyncio.sleep(0.4)
    await message.download(download_path, block = False)
    await message.delete()

# Video
@app.on_message(filters.video)
async def download_video(client, message):
    global folder_name, last_forward_time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if not folder_name or (time() - last_forward_time > 30):
        folder_name = f"Video_{now.minute}_{message.video.file_name}"
        print(dt_string + " Carpeta: " + folder_name)
        last_forward_time = time()
    
    full_path = os.path.join(directorio_multimedia, folder_name)
    download_path = os.path.join(full_path, message.video.file_name)
    if time() - last_forward_time > 30: folder_name = ""
    print(" > " + message.video.file_name)
    await message.reply_text(" > " + message.video.file_name)
    await asyncio.sleep(0.4)
    await message.download(download_path, block = False)
    await message.delete()

# Imagen
@app.on_message(filters.photo)
async def download_photo(client, message):
    global folder_name, last_forward_time
    await asyncio.sleep(1)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if not folder_name or (time() - last_forward_time > 30):
        folder_name = f"Imagen_{now.minute}_{message.photo.file_unique_id}"
        print(dt_string + " Carpeta: " + folder_name)
        last_forward_time = time()
    
    full_path = os.path.join(directorio_multimedia, folder_name)
    download_path = os.path.join(full_path, message.photo.file_unique_id + ".jpg")
    if time() - last_forward_time > 30: folder_name = ""
    print(" > " + message.photo.file_unique_id)
    await message.reply_text(" > " + message.photo.file_unique_id)
    await asyncio.sleep(0.4)
    await message.download(download_path, block = False)
    await message.delete()

# Torrent
@app.on_message(filters.document)
async def download_document(client, message):
    global folder_name, last_forward_time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if message.document.file_name.endswith('.torrent'):
        download_path = os.path.join(directorio_torrent, message.document.file_name)
    else:
        if not folder_name or (time() - last_forward_time > 30):
            folder_name = f"Otros_{now.minute}_{message.document.file_name.split('.')[0]}"
            print(dt_string + " Carpeta: " + folder_name)
            last_forward_time = time()
            
        full_path = os.path.join(directorio_multimedia, folder_name)
        download_path = os.path.join(full_path, message.document.file_name)
        if time() - last_forward_time > 30: folder_name = ""
    print( " : " + message.document.file_name)
    await message.reply_text(" : " + message.document.file_name)
    await asyncio.sleep(0.4)
    await message.download(download_path, block = False)
    await message.delete()

# No reconocido
@app.on_message(filters.media)
async def download(client, message):
      print("No soportado : ", message.media)

# Eco
@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)
    sleep(3)
    await message.delete()
###


app.run()