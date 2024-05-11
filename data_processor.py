import pandas as pd


class DataProcessor:
    def __init__(self, owned_games_df, all_games_df, top_sellers_df):
        self.owned_games_df = owned_games_df
        self.all_games_df = all_games_df
        self.top_sellers_df = top_sellers_df

    def process(self):
        # Map appid in owned games to names using all_games_df mapping
        game_id_to_name = pd.Series(
            self.all_games_df['name'].values, index=self.all_games_df['appid']
        ).to_dict()
        self.owned_games_df['name'] = self.owned_games_df['appid'].map(game_id_to_name)

        # Identify top sellers not owned by the user
        owned_game_ids = set(self.owned_games_df['appid'])
        recommended_games = self.top_sellers_df[
            ~self.top_sellers_df['appid'].isin(owned_game_ids)
        ]

        return recommended_games
