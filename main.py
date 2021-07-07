import discord
from discord.ext import commands

from environment import get_env

# intents = discord.Intents.default()
# intents.members = True

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('ready-v0.01')


if __name__ == '__main__':
    client.run(get_env().DISCORD_BOT_TOKEN)


