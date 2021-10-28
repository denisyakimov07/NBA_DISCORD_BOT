import datetime
import re

import discord

from data_base import NBA_Player
from data_base_function import get_discord_user_name

timezone_offset = 8.0  # Pacific Standard Time (UTC−08:00)
tzinfo = datetime.timezone(datetime.timedelta(hours=timezone_offset))


def player_data_card(player, ctx):
    embed = discord.Embed(title=f"{player.player_name}",
                          colour=discord.Colour(0x9f57a8),
                          url=f"{player.url}",
                          description=f"```{player.player_position} - {player.player_shoots}```",
                          timestamp=datetime.datetime.now(tzinfo))

    if player.players_photo_url:
        embed.set_thumbnail(url=player.players_photo_url)

    if player.player_pronunciation:
        embed.add_field(name="Pronunciation:", value=player.player_pronunciation, inline=False)

    if player.data_birth:
        embed.add_field(name="Born date:", value=f"{player.data_birth}", inline=True)

    if player.player_birth_city:
        embed.add_field(name="Place:", value=f"{player.player_birth_city}", inline=True)

    if player.player_born_name:
        embed.add_field(name="Born name:", value=f"{player.player_born_name}", inline=False)

    if player.player_career_length:
        embed.add_field(name="Career length:", value=f"{player.player_career_length}", inline=False)

    if player.player_height:
        embed.add_field(name="Height:", value=player.player_height, inline=True)

    if player.player_weight:
        embed.add_field(name="Weight:", value=player.player_weight, inline=True)

    if player.player_nba_debut:
        embed.add_field(name="Debut:", value=player.player_nba_debut, inline=False)

    if player.player_college:
        embed.add_field(name="College:", value=player.player_college, inline=True)

    if player.high_school:
        embed.add_field(name="School:", value=player.high_school, inline=True)

    if player.player_hall_of_fame:
        embed.add_field(name="Hall_of_fame:", value=player.player_hall_of_fame, inline=False)

    if player.player_draft:
        embed.add_field(name="Draft:", value=player.player_draft, inline=False)

    embed.set_footer(text=ctx.author, icon_url=f"{ctx.author.avatar_url}")

    return embed


def q1(player: NBA_Player):

    embed = discord.Embed(title = f"What year was {player.first_name} {player.last_name} drafted?",
                          colour = discord.Colour(0x9f57a8),
                          description = f"```Only accept numeric 4 number answers.```" ,
                          timestamp = datetime.datetime.now(tzinfo))


    embed.add_field(name="Answer ", value=player.draft_year ,inline=False)



    if player.players_photo_url:
        embed.set_thumbnail(url=player.players_photo_url)

    if player.player_pronunciation:
        embed.add_field(name="Pronunciation:", value=player.player_pronunciation, inline=False)

    if player.data_birth:
        embed.add_field(name="Born date:", value=f"{player.data_birth}", inline=True)

    if player.player_birth_city:
        embed.add_field(name="Place:", value=f"{player.player_birth_city}", inline=True)

    if player.player_born_name:
        embed.add_field(name="Born name:", value=f"{player.player_born_name}", inline=False)

    if player.player_career_length:
        embed.add_field(name="Career length:", value=f"{player.player_career_length}", inline=False)

    if player.player_height:
        embed.add_field(name="Height:", value=player.player_height, inline=True)

    if player.player_weight:
        embed.add_field(name="Weight:", value=player.player_weight, inline=True)

    if player.player_college:
        embed.add_field(name="College:", value=player.player_college, inline=True)

    if player.high_school:
        embed.add_field(name="School:", value=player.high_school, inline=True)

    if player.hall_of_fame_year and player.hall_of_fame_type:
        embed.add_field(name="Hall_of_fame:",
                        value=f"{player.hall_of_fame_year} - {player.hall_of_fame_type}",
                        inline=False)

    return embed


def wrong_guess(user_guess_list):
    embed = discord.Embed(colour=discord.Colour(0x3218ab))
    for user_guess in user_guess_list:
        value = str(user_guess_list[user_guess]).replace("[","").replace("]","").replace("'","")
        embed.add_field(name=f"{get_discord_user_name(user_guess)} - {len(user_guess_list[user_guess])}", value=value, inline=False)

    return embed