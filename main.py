import discord
from discord.ext import commands

from data_base import get_user_list_data, get_player_name_and_list_from_db
from environment import get_env
from fuz import spelling_check

client = commands.Bot(command_prefix='!')




@client.command()
async def name(ctx: discord.ext.commands.Context):
    player_name = str(ctx.message.content).replace("!name", "").strip()
    matches_names_list = spelling_check(names_list=get_player_name_and_list_from_db(), name=player_name)
    for i in get_user_list_data(matches_names_list):
        await ctx.send(i)
        await ctx.send("*************")



@client.event
async def on_ready():
    print('ready-v0.03')


if __name__ == '__main__':
    client.run(get_env().DISCORD_BOT_TOKEN)
