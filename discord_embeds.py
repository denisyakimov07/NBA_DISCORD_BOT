import datetime

import discord

from environment import get_env

timezone_offset = 8.0  # Pacific Standard Time (UTC−08:00)
tzinfo = datetime.timezone(datetime.timedelta(hours=timezone_offset))


def player_data_card(player):
    embed = discord.Embed(title=f"{player.player_name[0]}",
                                  colour=discord.Colour(0x9f57a8),
                                  url=f"{player.url[0]}",
                                  description="n. ```******```",
                                  timestamp=datetime.datetime.utcfromtimestamp(1626106534))
    if player.players_photo_url[0]:
        embed.set_thumbnail(url=player.players_photo_url)

    return embed






# def registered_user_embed(member: discord.Member):
#     embed = discord.Embed(colour=discord.Colour(0xff001f),
#                           description=f'<@!{member.id}> You must be a registered user to submit proof. '
#                                       f'Please check your messages for more details.',
#                           timestamp=datetime.datetime.now(tzinfo))
#     return embed
