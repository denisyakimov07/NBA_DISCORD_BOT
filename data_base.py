from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, load_only

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


def get_player_name_and_list_from_db():
    new_dict = {}
    players = session.query(Player).options(load_only('id', 'player_name')).all()
    for player in players:
        new_dict.update({f"{player.player_name}": int(player.id)})
    return new_dict


def get_number_of_rows():
    rows = session.query(Player).count()
    return rows


def get_user_fom_db_by_name(player_name_) -> dict:
    player_data_from_db = session.query(Player).filter_by(player_name=player_name_).all()
    return player_data_from_db[0].__dict__


def get_user_list_data(matches_names) -> list:
    player_data_list = []
    for name in matches_names:
        player_data = get_user_fom_db_by_name(name)
        player_data_list.append(player_data)
    return player_data_list


test_list = get_player_name_and_list_from_db()
matches_names_list = spelling_check(names_list=test_list, name="Jaylen")

for i in get_user_list_data(matches_names_list):
    print(i)
