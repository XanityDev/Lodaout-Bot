# Python Modules:
import discord

# Token:
BOT_TOKEN = 'ODkyNTczMTA2MTkzOTY5MTky.YVO3ew.JBO4VC_-CVuJAa_tHhnqYIojfw8'

# Set Client:
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}.'.format(client))

@client.event
async def on_message(message):
    if message.content == client.user:
        return

    # Test Message:
    if message.content.startswith('wz/test'):
        await message.channel.send('Work\'s!')

client.run(BOT_TOKEN)
