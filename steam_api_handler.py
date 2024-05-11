import requests
import pandas as pd


class SteamAPIHandler:
    def __init__(self, config):
        self.config = config

    def fetch_owned_games(self):
        response = requests.get(self.config.owned_games_url)
        if response.status_code == 200:
            data = response.json()
            games_data = data['response']['games']
            return pd.DataFrame(games_data)
        else:
            print(f"Error fetching owned games: {response.status_code}")
            return pd.DataFrame()

    def fetch_all_games(self):
        response = requests.get(self.config.all_games_url)
        if response.status_code == 200:
            data = response.json()
            games_data = data['applist']['apps']
            return pd.DataFrame(games_data)
        else:
            print(f"Error fetching all games: {response.status_code}")
            return pd.DataFrame()
