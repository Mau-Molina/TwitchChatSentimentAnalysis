# TwitchChatSentimentAnalysis
la idea GENERAL aqui es la siguiente

1- Usando un api TwitchIO de twitch, obtener como texto el chat durante un stream
2- mandar esta captura "stream" como archivos a gcs bucket
3- un beam que está monitoreando constantemente ese bucket, manda el texto al api de vertex text sentiment analysis y coloca los resultados en bq
4- visualizacion de resultados en dashboard


SNIPPETS

import twitchio

class Bot(twitchio.Client):
    def __init__(self):
        # Set up your Twitch credentials
        # Replace 'YOUR_USERNAME' and 'YOUR_OAUTH_TOKEN' with your Twitch username and OAuth token
        super().__init__(token='YOUR_OAUTH_TOKEN', prefix='!', initial_channels=['YOUR_USERNAME'])

    async def event_ready(self):
        print(f'Bot is connected to Twitch and ready to capture chat.')

    async def event_message(self, message):
        # Print the username and message content of each chat message
        print(f'{message.author.name}: {message.content}')

        # You can perform any desired processing or analysis of the chat messages here

        # Respond to a specific message in chat
        if message.content.lower() == '!hello':
            await message.channel.send(f'Hello, {message.author.name}!')

        # Send a message to the same channel where the command was triggered
        if message.content.lower() == '!ping':
            await message.channel.send('Pong!')

# Create an instance of the Bot class and run it
bot = Bot()
bot.run()


