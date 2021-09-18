import discord
import os
import base64
from dotenv import load_dotenv
import requests

# ===== HELPER FUNCTIONS =====
def get_quote():
  quote_data = requests.get("https://api.quotable.io/random").json()
  
  def get_tags():
    tags_list = quote_data['tags']
    
    if (len(tags_list) <= 1):
      return tags_list[0]
    
    tags = ""
    for tag in tags_list:
      tags += f"{tag}, "
    tags = tags.rstrip()[:-1]
    
    return tags
  
  tags = get_tags()
  quote_content = quote_data['content']
  quote_author = quote_data['author']
  
  full_quote = f'''
  {quote_content} ({tags})
  - {quote_author}
  '''
  
  return full_quote



# Create discord client
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
  
  quote = get_quote()
  if message.content.startswith('$quote'):
    await message.channel.send(quote)

# Load env vars
load_dotenv()
discordToken = base64.b64decode(os.getenv("TOKEN")).decode("utf-8")
client.run(discordToken)