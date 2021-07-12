import datetime

import discord

timezone_offset = 8.0  # Pacific Standard Time (UTC−08:00)
tzinfo = datetime.timezone(datetime.timedelta(hours=timezone_offset))


def player_data_card(player):
    embed = discord.Embed(title=f"{player.player_name}",
                          colour=discord.Colour(0x9f57a8),
                          url=f"{player.url}",
                          description=f"```{player.player_position} - {player.player_shoots}```",
                          timestamp=datetime.datetime.utcfromtimestamp(1626106534))

    if player.players_photo_url:
        embed.set_thumbnail(url=player.players_photo_url)

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

    if player.player_pronunciation:
        embed.add_field(name="Pronunciation:", value=player.player_pronunciation, inline=False)

    if player.player_hall_of_fame:
        embed.add_field(name="Hall_of_fame:", value=player.player_hall_of_fame, inline=False)

    if player.player_draft:
        embed.add_field(name="Draft:", value=player.player_draft, inline=False)

    return embed
