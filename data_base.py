from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, Text
from sqlalchemy.orm import declarative_base, sessionmaker


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

# test_list = get_player_name_and_list_from_db()

# for i in test_list:
#     print(i)



# matches_names_list = spelling_check(names_list=test_list, name="Jaylen")
