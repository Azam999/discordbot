import discord
import os
import base64
from dotenv import load_dotenv

client = discord.Client()

# Runs when bot initializes
@client.event
async def on_ready():
  print(f'''
        Bot is ready
        User: {client.user}
        ''')

# Runs when user send a message
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$quote'):
    await message.channel.send("joke")

# Load env vars
load_dotenv()
discordToken = base64.b64decode(os.getenv("TOKEN")).decode("utf-8")
client.run(discordToken)