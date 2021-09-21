from data_base import session, Player, Base, Quiz_Question


def get_player_name_and_list_from_db() -> list[Player]:
    players = session.query(Player).all()
    return players


def get_players_draft_list_from_db() -> list[Player]:
    players = session.query(Player).filter(Player.player_draft != None ).all()
    return players

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

def create_new_tables(engine_db):
    Base.metadata.create_all(engine_db)
# create_new_tables(engine)

def get_not_close_from_db() -> Quiz_Question:
    quiz_question = session.query(Quiz_Question).filter_by(status=True).first()
    return quiz_question
