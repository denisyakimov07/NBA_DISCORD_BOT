import random
import re

import discord
from discord.ext import commands

from data_base import Quiz_Question, Session
from data_base_function import get_user_list_data, get_player_name_and_list_from_db, get_players_draft_list_from_db, \
    get_not_close_from_db
from discord_embeds import player_data_card, q1
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
async def q(ctx: discord.ext.commands.Context):
    if get_not_close_from_db() == None:
        player_for_q = random.choice(get_players_draft_list_from_db())
        message = await ctx.send(embed=q1(player=player_for_q))

        match = re.search('\d{4}', player_for_q.player_draft)
        year = match.group(0)

        quiz = Quiz_Question()
        quiz.player_id = player_for_q.id
        quiz.message_id = message.id
        quiz.right_answer = year
        quiz.jump_url = message.jump_url

        session = Session()
        session.add(quiz)
        session.commit()
        session.close()
        await message.pin()
    else:
        pass

        # mes = await ctx.fetch_message(id=889735210764234783)
        # print(mes.content)







@client.command()
async def clear(ctx: discord.ext.commands.Context, amount=0):
    await ctx.channel.purge(limit=amount + 1)


@client.event
async def on_ready():
    version = 'ready-v0.06'
    channel = client.get_channel(id=765713378210611261)
    await channel.send(version)
    print(version)


if __name__ == '__main__':
    client.run(get_env().DISCORD_BOT_TOKEN)
