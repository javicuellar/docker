from pyrogram import Client
import asyncio



api_id = 123456  # Reemplaza con tu API ID
api_hash = "your_api_hash"  # Reemplaza con tu API Hash


async def crear_grupo():
    async with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        yo = await app.get_me()
        grupo = await app.create_group("Nuevo Grupo", [yo.id], description="Descripción del grupo")
        print(f"Grupo creado: {grupo.title} con ID {grupo.id}")



if __name__ == "__main__":
    asyncio.run(crear_grupo())
