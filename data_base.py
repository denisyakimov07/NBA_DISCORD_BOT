from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, Text, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

from environment import get_env
from fuz import spelling_check

engine_config = \
    f'{get_env().DB_DATABASE_TYPE}:' \
    f'//{get_env().DB_USER}:' \
    f'{get_env().DB_PASSWORD}@' \
    f'{get_env().DB_HOST}:5432/' \
    f'{get_env().DB_DATABASE}'

engine = create_engine(engine_config, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Player(Base):
    __tablename__ = 'nba-player'

    id = Column(Integer, primary_key=True)
    player_name = Column(String(300))
    url = Column(String(300))
    player_pronunciation = Column(String(300))
    player_position = Column(String(300))
    player_shoots = Column(String(300))
    player_height = Column(String(300))
    player_weight = Column(String(300))
    data_birth = Column(String(300))
    player_birth_city = Column(String(300))
    player_college = Column(String(300))
    high_school = Column(String(300))
    player_draft = Column(String(300))
    player_nba_debut = Column(String(300))
    player_career_length = Column(String(300))
    player_born_name = Column(String(300))
    player_hall_of_fame = Column(String(300))
    players_photo_url = Column(String(300))

class Quiz_Question(Base):
    __tablename__ = 'quiz_question'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer)
    status = Column(Boolean, default=False)
    message_id = Column(BigInteger)
    right_answer = Column(String(300))
    jump_url = Column(Text)
    discord_wrong_collect_mg_id = Column(BigInteger)

class Guess(Base):
    __tablename__ = 'guess'
    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer)
    status = Column(Boolean, default=False)
    discord_user_id = Column(BigInteger)
    discord_user_name = Column(String(300))
    user_guess = Column(Text)

class NBA_Player(Base):
    __tablename__ = 'nba_player'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(300))
    last_name = Column(String(300))
    url = Column(String(300))
    player_pronunciation = Column(String(300))
    player_position = Column(String(300))
    player_shoots = Column(String(300))
    player_height = Column(String(300))
    data_birth = Column(String(300))
    player_birth_city = Column(String(300))
    player_born_name = Column(String(300))
    players_photo_url = Column(String(300))
    hall_of_fame_year = Column(String(300))
    hall_of_fame_type = Column(String(300))
    player_career_length = Column(String(300))
    professional_debut = Column(String(300))
    player_shoots = Column(String(300))
    draft_team = Column(String(300))
    draft_year = Column(Integer)
    draft_league = Column(String(300))
    draft_round = Column(String(300))
    draft_position = Column(String(300))
    draft_overall = Column(String(300))
    high_school = Column(String(300))
    player_college = Column(String(300))
    player_position = Column(String(300))
    player_weight = Column(String(300))
    status = Column(Boolean, default=False)

    children = relationship("NBA_Player_Stat")



class NBA_Player_Stat(Base):
    __tablename__ = 'player_stat'

    id = Column(Integer, primary_key=True)
    url = Column(String(300))
    player_name = Column(String(300))  # Player =
    games = Column(String(300))  # Games =
    games_started = Column(String(300))  # Games Started =
    minutes_played = Column(String(300))  # Minutes Played =
    field_goals = Column(String(300))  # Field Goals =
    field_goal_attempts = Column(String(300))  # Field Goal Attempts =
    field_goal_percentage = Column(String(300))  # Field Goal Percentage =
    point_field_goals_3 = Column(String(300))  # 3-Point Field Goals =
    point_field_goal_attempts_3 = Column(String(300))  # 3-Point Field Goal Attempts =
    point_field_goal_percentage_3 = Column(String(300))   # 3-Point Field Goal Percentage =
    point_field_goals_2 = Column(String(300))  # 2-Point Field Goals =
    point_field_goal_attempts_2 = Column(String(300))  # 2-point Field Goal Attempts =
    point_field_goal_percentage_2 = Column(String(300))  # 2-Point Field Goal Percentage =
    free_throws = Column(String(300))  # Free Throws =
    free_throw_attempts = Column(String(300))   # Free Throw Attempts =
    free_throw_percentage = Column(String(300))  # Free Throw Percentage =
    offensive_rebounds = Column(String(300))   # Offensive Rebounds =
    defensive_rebounds = Column(String(300))   # Defensive Rebounds
    total_rebounds = Column(String(300))    # Total Rebounds =
    assists = Column(String(300))    # Assists =
    steals = Column(String(300))   # Steals =
    blocks = Column(String(300))    # Blocks =
    turnovers = Column(String(300))    # Turnovers =
    personal_fouls = Column(String(300))  # Personal Fouls =
    points = Column(String(300))  # Points =
    minutes_played_per_game = Column(String(300))  # Minutes Played Per Game =
    points_per_game = Column(String(300))  # Points Per Game =
    total_rebounds_per_game = Column(String(300))  # Total Rebounds Per Game =
    assists_per_game = Column(String(300))  # Assists Per Game =

    parent_id = Column(Integer, ForeignKey('nba_player.id'))





# test_list = get_player_name_and_list_from_db()

# for i in test_list:
#     print(i)



# matches_names_list = spelling_check(names_list=test_list, name="Jaylen")
