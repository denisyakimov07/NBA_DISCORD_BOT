import discord
from discord.ext import commands

from environment import get_env

client = commands.Bot(command_prefix='!')




@client.command()

async def name(ctx: discord.ext.commands.Context):
    print(ctx)
    # await ctx.channel.purge(limit=amount + 1)



@client.event
async def on_ready():
    print('ready-v0.02')


if __name__ == '__main__':
    client.run(get_env().DISCORD_BOT_TOKEN)


