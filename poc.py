from twitchio.ext import commands
from dotenv import dotenv_values

config = dotenv_values(".env")
# leer la configuracion desde el archivo .env
bot_token = config['TWITCH_OAUTH_TOKEN']

# se puede setear una lista de canales
bot_channels = ['diegoruzzarin']


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=bot_token, prefix='?', initial_channels=bot_channels)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.author)
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

bot = Bot()
bot.run()