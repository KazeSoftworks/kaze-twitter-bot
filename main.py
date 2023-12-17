import discord
from decouple import config
from urllib.parse import urlparse, urlunparse
import re

TOKEN = config('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
CLIENT = discord.Client(intents=intents)

@CLIENT.event
async def on_ready():
    print(f'We have logged in as {CLIENT.user}')

@CLIENT.event
async def on_message(message):
    # Revisa si el mensaje es del bot o no tenga contenido
    if message.author.bot or not message.content:
        return

    # Define la regular expression para que detecte URLs de Twitter y X 
    url_pattern = re.compile(r'(https?://(?:www\.)?(?:x\.com)/(?!home)[^\s/]*)')

    # Encuentra las coincidencias en el mensaje
    matches = url_pattern.findall(message.content)

    if matches:
        # Remplaza el dominio por el de vxtwitter
        for match in matches:
            parsed_url = urlparse(match)
            modified_url = urlunparse(parsed_url._replace(netloc='vxtwitter.com'))
            
            # Reemplaza la URL original por la modificada en el contenido del mensaje
            message.content = message.content.replace(match, modified_url)

        # Envia el mensaje modificado al canal
        await message.channel.send(message.content)

CLIENT.run(TOKEN)