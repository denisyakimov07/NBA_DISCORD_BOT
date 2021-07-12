import datetime

import discord

from environment import get_env

timezone_offset = 8.0  # Pacific Standard Time (UTC−08:00)
tzinfo = datetime.timezone(datetime.timedelta(hours=timezone_offset))


def player_data_card(player):
    embed = discord.Embed(title=f"{player.player_name[0]}",
                                  colour=discord.Colour(0x9f57a8),
                                  url=f"{player.url[0]}",
                                  description=f"```{player.player_position[0]} - {player.player_shoots[0]}```",
                                  timestamp=datetime.datetime.utcfromtimestamp(1626106534))
    if player.players_photo_url:
        embed.set_thumbnail(url=player.players_photo_url)

    if player.data_birth:
        embed.add_field(name="Born date:", value=f"{player.data_birth[0]}", inline=True)

    if player.player_birth_city:
        embed.add_field(name="Place:", value=f"{player.player_birth_city[0]}", inline=True)

    if player.player_born_name:
        embed.add_field(name="Born name:", value=f"{player.player_born_name[0]}", inline=False)

    if player.player_career_length:
        embed.add_field(name="Career length:", value=f"{player.player_career_length[0]}", inline=False)

    if player.player_height:
        embed.add_field(name="Height:", value=player.player_height[0], inline=True)

    if player.player_weight:
        embed.add_field(name="Weight:", value=player.player_weight[0], inline=True)

    return embed





# def registered_user_embed(member: discord.Member):
#     embed = discord.Embed(colour=discord.Colour(0xff001f),
#                           description=f'<@!{member.id}> You must be a registered user to submit proof. '
#                                       f'Please check your messages for more details.',
#                           timestamp=datetime.datetime.now(tzinfo))
#     return embed
