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
    name_list = [pl_name.player_name for pl_name in get_player_name_and_list_from_db()]
    matches_names_list = spelling_check(names_list=name_list, name=player_name)
    for i in get_user_list_data(matches_names_list):
        player = PlayerCard(i)
        await ctx.send(embed=player_data_card(player=player, ctx=ctx))
        await ctx.message.delete()







@client.command()
async def clear(ctx: discord.ext.commands.Context, amount=0):
    await ctx.channel.purge(limit=amount + 1)


@client.event
async def on_ready():
    channel = client.get_channel(id=765713378210611261)
    await channel.send('ready-v0.05')
    print('ready-v0.05')


if __name__ == '__main__':
    client.run(get_env().DISCORD_BOT_TOKEN)
