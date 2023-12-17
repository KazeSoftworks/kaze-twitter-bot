# Discord Bot con Modificación de URLs

Este es un simple bot de Discord escrito en Python utilizando la biblioteca `discord.py`. El bot detecta URLs de Twitter y X en los mensajes y las modifica reemplazando el dominio por el de `vxtwitter.com`. El cual en discord devuelve un mensaje embebido.

## Configuración

1. Asegúrate de tener Python instalado en tu sistema. Recomendado `python 3.10.12`
2. Clona este repositorio.
3. Inicializa un ambiente virtual

```bash
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

4. Crea un archivo `.env` en el directorio raiz del proyecto y agrega tu token de Discord, puedes ver `.env.example` como ejemplo

```bash
DISCORD_TOKEN=discord_token_aqui
```

## Uso

Ejecuta el script `main.py` para iniciar el bot:

```bash
python3 main.py
```

El bot estará activo y listo para modificar URLs en los mensajes de Discord.

## Generación de link invites

El bot debe tener permisos siguientes cuando se generen links de invitación:

- Scopes
  - bot
  - applications.commands
- Bot permissions
  - Send Messages
  - Read Messages

## Funcionamiento

El bot utiliza expresiones regulares para detectar URLs de Twitter y X en los mensajes. Luego, reemplaza el dominio por el de vxtwitter.com y envía el mensaje modificado de vuelta al canal.
