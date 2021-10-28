import discord

from data_base import NBA_Player, Quiz_Question, Session, session, NBA_Player
from data_base_function import get_not_close_quiz_from_db, get_players_draft_list_from_db, add_quiz_to_db, \
    add_guess_to_db, get_guess_to_db, get_player_name_and_list_from_db, get_user_list_data
from discord_embeds import q1, wrong_guess, player_data_card
from fuz import spelling_check
from helper import PlayerCard


async def create_new_quiz(ctx: discord.ext.commands.Context):
    quiz =  get_not_close_quiz_from_db()
    if quiz == None:
        player_for_q: NBA_Player = get_players_draft_list_from_db()
        message = await ctx.send(embed=q1(player=player_for_q))


        year = player_for_q.draft_year
        add_quiz_to_db(player_for_q=player_for_q, message=message, answer=year)

        await message.pin()
    else:
        await ctx.send(f"The quiz has already started go to {quiz.jump_url}")


async def checking_the_answer(ctx: discord.ext.commands.Context):
    user_guess = str(ctx.message.content).replace("!a", "").strip()
    quiz = get_not_close_quiz_from_db()
    if quiz:
        if str(quiz.right_answer) != str(user_guess):
            await ctx.send(f"{ctx.message.author.name} - {user_guess} is incorrect.")
            if quiz.discord_wrong_collect_mg_id:
                old_message = await ctx.fetch_message(id=quiz.discord_wrong_collect_mg_id)
                await old_message.delete()
            discord_user: discord.Member = ctx.message.author
            add_guess_to_db(discord_user=discord_user, user_guess=user_guess, quiz=quiz)
            user_guess_list = get_guess_to_db(quiz)
            message = await ctx.send(embed=wrong_guess(user_guess_list))
            quiz.discord_wrong_collect_mg_id = message.id
            session.commit()

    await ctx.message.delete()
    if quiz:
        if str(quiz.right_answer) == str(user_guess):
            quiz = get_not_close_quiz_from_db()
            mes = await ctx.fetch_message(id=quiz.message_id)
            await ctx.send(f"{ctx.message.author.name} - {user_guess} is right answer you win!")
            quiz.status = True
            session.commit()
            await mes.unpin()
            await create_new_quiz(ctx)

async def get_user_data_by_name(ctx: discord.ext.commands.Context):
    player_name = str(ctx.message.content).replace("!name", "").strip()
    name_list = [pl_name.player_name for pl_name in get_player_name_and_list_from_db()]
    matches_names_list = spelling_check(names_list=name_list, name=player_name)
    for i in get_user_list_data(matches_names_list):
        player = PlayerCard(i)
        await ctx.send(embed=player_data_card(player=player, ctx=ctx))
        await ctx.message.delete()