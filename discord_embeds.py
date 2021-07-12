import datetime

import discord

from environment import get_env

timezone_offset = 8.0  # Pacific Standard Time (UTC−08:00)
tzinfo = datetime.timezone(datetime.timedelta(hours=timezone_offset))


def player_data_card(member: discord.Member):
    pass






# def registered_user_embed(member: discord.Member):
#     embed = discord.Embed(colour=discord.Colour(0xff001f),
#                           description=f'<@!{member.id}> You must be a registered user to submit proof. '
#                                       f'Please check your messages for more details.',
#                           timestamp=datetime.datetime.now(tzinfo))
#     return embed
