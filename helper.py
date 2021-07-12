
class PlayerCard:

    def __init__(self, user_info_dict_to_class):
        self.player_name = user_info_dict_to_class.get("player_name")
        self.url = user_info_dict_to_class.get("url")
        self.player_pronunciation = user_info_dict_to_class.get("player_pronunciation")
        self.player_position = user_info_dict_to_class.get("player_position")
        self.player_shoots = user_info_dict_to_class.get("player_shoots")
        self.player_height = user_info_dict_to_class.get("player_height")
        self.player_weight = user_info_dict_to_class.get("player_weight")
        self.data_birth = user_info_dict_to_class.get("data_birth")
        self.player_birth_city = user_info_dict_to_class.get("player_birth_city")
        self.player_college = user_info_dict_to_class.get("player_college")
        self.high_school = user_info_dict_to_class.get("high_school")
        self.player_draft = user_info_dict_to_class.get("player_draft")
        self.player_nba_debut = user_info_dict_to_class.get("player_nba_debut")
        self.player_career_length = user_info_dict_to_class.get("player_career_length")
        self.player_born_name = user_info_dict_to_class.get("player_born_name")
        self.player_hall_of_fame = user_info_dict_to_class.get("player_hall_of_fame")
        self.players_photo_url = user_info_dict_to_class.get("players_photo_url")

        print(self.player_name),
        print(self.url),
        print(self.player_pronunciation),
        print(self.player_position),
        print(self.player_shoots),
        print(self.player_height),
        print(self.player_weight),
        print(self.data_birth),
        print(self.player_birth_city),
        print(self.player_college),
        print(self.high_school),
        print(self.player_draft),
        print(self.player_nba_debut),
        print(self.player_career_length),
        print(self.player_born_name),
        print(self.player_hall_of_fame),
        print(self.players_photo_url)