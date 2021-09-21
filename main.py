import random
import re

import discord
from discord.ext import commands

from data_base import Quiz_Question, Session
from data_base_function import get_user_list_data, get_player_name_and_list_from_db, get_players_draft_list_from_db, \
    get_not_close_quiz_from_db, add_quiz_to_db
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
    quiz =  get_not_close_quiz_from_db()
    if quiz == None:
        player_for_q = random.choice(get_players_draft_list_from_db())
        message = await ctx.send(embed=q1(player=player_for_q))

        match = re.search('\d{4}', player_for_q.player_draft)
        year = match.group(0)
        add_quiz_to_db(player_for_q=player_for_q, message=message, answer=year)

        await message.pin()
    else:
        await ctx.send(f"The quiz has already started go to {quiz.jump_url}")

        # mes = await ctx.fetch_message(id=889735210764234783)
        # print(mes.content)


@client.command()
async def g(ctx: discord.ext.commands.Context):
    user_guess = str(ctx.message.content).replace("!g", "").strip()
    quiz = get_not_close_quiz_from_db()
    if str(quiz.right_answer) != str(user_guess):
        await ctx.send(f"{ctx.message.author.name} - {user_guess} is wrong answer.")
        await ctx.message.delete()

    if str(quiz.right_answer) == str(user_guess):
        await ctx.send(f"{ctx.message.author.name} - {user_guess} is right answer you win!")
        await ctx.message.delete()






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
