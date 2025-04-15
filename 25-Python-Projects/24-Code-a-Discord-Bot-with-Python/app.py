import discord
import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env

# Set up the intents
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

token = os.environ.get('DISCORD_TOKEN')
if token is None:
    print("Error: DISCORD_TOKEN environment variable not set!")
else:
    client.run(token)
