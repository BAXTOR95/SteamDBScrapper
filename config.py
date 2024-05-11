class Config:
    def __init__(self, api_key, steam_id):
        self.api_key = api_key
        self.steam_id = steam_id
        self.owned_games_url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={self.api_key}&steamid={self.steam_id}&format=json"
        self.all_games_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
