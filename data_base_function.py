import random

import discord
from tqdm import tqdm

from career_stats_scrap import get_player_stat_from_site
from data_base import session, Player, Base, Quiz_Question, Session, Guess, NBA_Player, NBA_Player_Stat

from collections import defaultdict

def get_player_name_and_list_from_db() -> list[Player]:
    players = session.query(Player).all()
    return players


def get_players_draft_list_from_db() -> NBA_Player:
    players: list[NBA_Player] = session.query(NBA_Player).filter(NBA_Player.draft_year != None, NBA_Player.status == True).all()
    return random.choice(players)

def get_number_of_rows():
    rows = session.query(Player).count()
    return rows


def get_user_fom_db_by_name(player_name) -> dict:
    player_data_from_db = session.query(Player).filter_by(player_name=player_name).all()
    return player_data_from_db[0].__dict__


def get_user_list_data(matches_names) -> list:
    player_data_list = []
    for name in matches_names:
        player_data = get_user_fom_db_by_name(name)
        player_data_list.append(player_data)
    return player_data_list

def create_new_tables(engine_db):
    Base.metadata.create_all(engine_db)
# create_new_tables(engine)

def get_not_close_quiz_from_db() -> Quiz_Question:
    quiz_question = session.query(Quiz_Question).filter_by(status=False).first()
    return quiz_question


def create_quiz():
    if get_not_close_quiz_from_db():
        return False

def add_quiz_to_db(player_for_q,message,answer):
    quiz = Quiz_Question()
    quiz.player_id = player_for_q.id
    quiz.message_id = message.id
    quiz.right_answer = answer
    quiz.jump_url = message.jump_url

    session = Session()
    session.add(quiz)
    session.commit()
    session.close()

def add_guess_to_db(discord_user: discord.Member , user_guess: str, quiz: Quiz_Question(), status = False):
    guess = Guess()
    guess.discord_user_id = discord_user.id
    guess.discord_user_name = discord_user.name
    guess.user_guess = user_guess
    guess.quiz_id = quiz.id
    guess.status = status

    session = Session()
    session.add(guess)
    session.commit()
    session.close()

def get_guess_to_db(quiz: Quiz_Question()):

    user_guess_list_object = session.query(Guess).filter_by(quiz_id = quiz.id).all()
    users_list = [user_guess.discord_user_id for user_guess in user_guess_list_object]
    user_guess_set = dict.fromkeys(set(users_list))
    user_guess = [[user_guess.discord_user_id, user_guess.user_guess] for user_guess in user_guess_list_object]

    for user in set(users_list):
        ls = []
        for x in user_guess:
            if user == x[0]:
                ls.append(x[1])
        user_guess_set[user] = ls

    return user_guess_set

def get_discord_user_name(discord_user_id):
    name = session.query(Guess).filter_by(discord_user_id = discord_user_id).first().discord_user_name
    return name


def players_from_db():
    player_data_from_db = session.query(NBA_Player).all()
    return player_data_from_db

def nba_players_from_db(url):
    player_data_from_db = session.query(NBA_Player).filter_by(url = url).first()
    return player_data_from_db

def change_player_height():
    count = len(players_from_db())
    pbar = tqdm(total=count)
    for player in players_from_db():
        player.player_height = nba_players_from_db(player.url).player_height
        pbar.update(1)

    session.commit()




def add_player_stat_to_db():
    players = get_player_stat_from_site()
    pbar = tqdm(total=len(players))
    session = Session()


    for player in players:
        player_stat = NBA_Player_Stat()
        player_stat.url = player["url"]
        player_stat.player_name = player["player_name"]
        player_stat.games = player["games"]
        player_stat.games_started = player["games_started"]
        player_stat.minutes_played = player["minutes_played"]
        player_stat.field_goals = player["field_goals"]
        player_stat.field_goal_attempts = player["field_goal_attempts"]
        player_stat.field_goal_percentage = player["field_goal_percentage"]
        player_stat.point_field_goal_attempts_3 = player["point_field_goal_attempts_3"]
        player_stat.point_field_goal_percentage_3 = player["point_field_goal_percentage_3"]
        player_stat.point_field_goals_3 = player["point_field_goals_3"]
        player_stat.point_field_goals_2 = player["point_field_goals_2"]
        player_stat.point_field_goal_attempts_2 = player["point_field_goal_attempts_2"]
        player_stat.point_field_goal_percentage_2 = player["point_field_goal_percentage_2"]
        player_stat.free_throws = player["free_throws"]
        player_stat.free_throw_attempts = player["free_throw_attempts"]
        player_stat.free_throw_percentage = player["free_throw_percentage"]
        player_stat.offensive_rebounds = player["offensive_rebounds"]
        player_stat.defensive_rebounds = player["defensive_rebounds"]
        player_stat.total_rebounds = player["total_rebounds"]
        player_stat.assists = player["assists"]
        player_stat.steals = player["steals"]
        player_stat.blocks = player["blocks"]
        player_stat.turnovers = player["turnovers"]
        player_stat.personal_fouls = player["personal_fouls"]
        player_stat.points = player["points"]
        player_stat.minutes_played_per_game = player["minutes_played_per_game"]
        player_stat.points_per_game = player["points_per_game"]
        player_stat.total_rebounds_per_game = player["total_rebounds_per_game"]
        player_stat.assists_per_game = player["assists_per_game"]

        nba_players: NBA_Player = nba_players_from_db(player["url"])
        # print(player_stat.url)
        # print(nba_players.url)

        player_stat.parent_id = nba_players.id


        session.add(player_stat)
        pbar.update(1)
    session.commit()

def nba_player_stat_change():
    session = Session()
    players_stat= session.query(NBA_Player_Stat).all()
    pbar = tqdm(total=len(players_stat))
    for player in players_stat:
        nba_pl = session.query(NBA_Player).filter_by(url = player.url).first()
        nba_pl.status = True
        pbar.update(1)
    session.commit()

