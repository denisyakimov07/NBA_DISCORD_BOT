import discord
from discord.ext import commands

from data_base import get_user_list_data, get_player_name_and_list_from_db
from discord_embeds import player_data_card
from environment import get_env
from fuz import spelling_check
from helper import PlayerCard

client = commands.Bot(command_prefix='!')




@client.command()
async def name(ctx: discord.ext.commands.Context):
    player_name = str(ctx.message.content).replace("!name", "").strip()
    matches_names_list = spelling_check(names_list=get_player_name_and_list_from_db(), name=player_name)
    for i in get_user_list_data(matches_names_list):
        player = PlayerCard(i)
        await ctx.send(embed=player_data_card(player))




@client.event
async def on_ready():
    print('ready-v0.05')


if __name__ == '__main__':
    client.run(get_env().DISCORD_BOT_TOKEN)
