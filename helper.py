
class PlayerCard:

    def __init__(self, user_info_dict_to_class):
        self.player_name = user_info_dict_to_class.get("player_name", None)
        self.url = user_info_dict_to_class.get("url", None)
        self.player_pronunciation = user_info_dict_to_class.get("player_pronunciation", None)
        self.player_position = user_info_dict_to_class.get("player_position", None)
        self.player_shoots = user_info_dict_to_class.get("player_shoots", None)
        self.player_height = user_info_dict_to_class.get("player_height", None)
        self.player_weight = user_info_dict_to_class.get("player_weight", None)
        self.data_birth = user_info_dict_to_class.get("data_birth", None)
        self.player_birth_city = user_info_dict_to_class.get("player_birth_city", None)
        self.player_college = user_info_dict_to_class.get("player_college", None)
        self.high_school = user_info_dict_to_class.get("high_school", None)
        self.player_draft = user_info_dict_to_class.get("player_draft", None)
        self.player_nba_debut = user_info_dict_to_class.get("player_nba_debut", None)
        self.player_career_length = user_info_dict_to_class.get("player_career_length", None)
        self.player_born_name = user_info_dict_to_class.get("player_born_name", None)
        self.player_hall_of_fame = user_info_dict_to_class.get("player_hall_of_fame", None)
        self.players_photo_url = user_info_dict_to_class.get("players_photo_url", None)