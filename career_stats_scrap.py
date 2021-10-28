from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

URL = 'https://www.basketball-reference.com/allstar/NBA-allstar-career-stats.html'
BASE_URL = 'https://www.basketball-reference.com'



def get_player_stat_from_site() -> list[dict]:
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    table_head: list[BeautifulSoup] = soup.find("tbody").find_all(attrs={"data-row":""}, recursive=False)
    res = []
    for pl in table_head:
        if pl.find(attrs={"data-stat":"player"}) and pl.find("a"):
           url =  f'{BASE_URL}{pl.find("a").get("href")}'
           player_name = pl.find(attrs={"data-stat":"player"}).text #Player =
           games = pl.find(attrs={"data-stat":"g"}).text#Games =
           games_started = pl.find(attrs={"data-stat":"gs"}).text#Games Started =
           minutes_played = pl.find(attrs={"data-stat":"mp"}).text#Minutes Played =
           field_goals = pl.find(attrs={"data-stat":"fg"}).text#Field Goals =
           field_goal_attempts = pl.find(attrs={"data-stat":"fga"}).text#Field Goal Attempts =
           field_goal_percentage = pl.find(attrs={"data-stat":"fg_pct"}).text#Field Goal Percentage =
           point_field_goals_3 = pl.find(attrs={"data-stat":"fg3"}).text#3-Point Field Goals =
           point_field_goal_attempts_3 = pl.find(attrs={"data-stat":"fg3a"}).text#3-Point Field Goal Attempts =
           point_field_goal_percentage_3 = pl.find(attrs={"data-stat":"fg3_pct"}).text #3-Point Field Goal Percentage =
           point_field_goals_2 = pl.find(attrs={"data-stat":"fg2"}).text#2-Point Field Goals =
           point_field_goal_attempts_2 = pl.find(attrs={"data-stat":"fg2a"}).text#2-point Field Goal Attempts =
           point_field_goal_percentage_2 = pl.find(attrs={"data-stat":"fg2_pct"}).text#2-Point Field Goal Percentage =
           free_throws = pl.find(attrs={"data-stat":"ft"}).text#Free Throws =
           free_throw_attempts = pl.find(attrs={"data-stat":"fta"}).text#Free Throw Attempts =
           free_throw_percentage = pl.find(attrs={"data-stat":"ft_pct"}).text#Free Throw Percentage =
           offensive_rebounds = pl.find(attrs={"data-stat":"orb"}).text#Offensive Rebounds =
           defensive_rebounds = pl.find(attrs={"data-stat":"drb"}).text#Defensive Rebounds
           total_rebounds = pl.find(attrs={"data-stat":"trb"}).text#Total Rebounds =
           assists = pl.find(attrs={"data-stat":"ast"}).text#Assists =
           steals = pl.find(attrs={"data-stat":"stl"}).text#Steals =
           blocks = pl.find(attrs={"data-stat":"blk"}).text#Blocks =
           turnovers = pl.find(attrs={"data-stat":"tov"}).text#Turnovers =
           personal_fouls = pl.find(attrs={"data-stat":"pf"}).text#Personal Fouls =
           points = pl.find(attrs={"data-stat":"pts"}).text#Points =
           minutes_played_per_game = pl.find(attrs={"data-stat":"mp_per_g"}).text#Minutes Played Per Game =
           points_per_game = pl.find(attrs={"data-stat":"pts_per_g"}).text#Points Per Game =
           total_rebounds_per_game = pl.find(attrs={"data-stat":"trb_per_g"}).text#Total Rebounds Per Game =
           assists_per_game = pl.find(attrs={"data-stat":"ast_per_g"}).text#Assists Per Game =

           res.append({"url": url, "player_name": player_name, "games": games, "games_started": games_started,
                       "minutes_played": minutes_played, "field_goals": field_goals,
                       "field_goal_attempts": field_goal_attempts, "field_goal_percentage": field_goal_percentage,
                       "point_field_goals_3":point_field_goals_3, "point_field_goal_attempts_3": point_field_goal_attempts_3,
                       "point_field_goal_percentage_3": point_field_goal_percentage_3, "point_field_goals_2": point_field_goals_2,
                       "point_field_goal_attempts_2": point_field_goal_attempts_2,
                       "point_field_goal_percentage_2": point_field_goal_percentage_2, "free_throws": free_throws,
                       "free_throw_attempts": free_throw_attempts, "free_throw_percentage": free_throw_percentage,
                       "offensive_rebounds": offensive_rebounds, "defensive_rebounds": defensive_rebounds,
                       "total_rebounds": total_rebounds, "assists": assists, "steals": steals, "blocks": blocks,
                       "turnovers": turnovers, "personal_fouls": personal_fouls, "points": points,
                       "minutes_played_per_game": minutes_played_per_game, "points_per_game": points_per_game,
                       "total_rebounds_per_game": total_rebounds_per_game, "assists_per_game": assists_per_game})
    return res