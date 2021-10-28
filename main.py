import discord
from discord.ext import commands

from data_base import Quiz_Question, Session, session, NBA_Player
from data_base_function import get_user_list_data, get_player_name_and_list_from_db, get_players_draft_list_from_db, \
    get_not_close_quiz_from_db, add_quiz_to_db, add_guess_to_db, get_guess_to_db
from discord_embeds import player_data_card, q1, wrong_guess
from discord_functions import create_new_quiz, checking_the_answer, get_user_data_by_name
from environment import get_env
from fuz import spelling_check
from helper import PlayerCard

client = commands.Bot(command_prefix='!')




@client.command(brief='Return NBA Player data.', description='Return NBA Player data.')
async def name(ctx: discord.ext.commands.Context):
    await get_user_data_by_name(ctx)



@client.command(brief="Start new quiz.")
async def q(ctx: discord.ext.commands.Context):
    await create_new_quiz(ctx)

@client.command(brief="Add your answer to an open quiz", description="Add your answer to an open quiz")
async def a(ctx: discord.ext.commands.Context):
    await checking_the_answer(ctx)











@client.command(brief="Delete messages",description='Delete the specified number of messages in the channel [!clear 5]')
async def clear(ctx: discord.ext.commands.Context, amount=0):
    await ctx.channel.purge(limit=amount + 1)


@client.event
async def on_ready():
    version = 'ready-v0.06'
    print(version)


if __name__ == '__main__':
    client.run(get_env().DISCORD_BOT_TOKEN)
