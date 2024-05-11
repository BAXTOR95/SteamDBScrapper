import os
import dotenv
import argparse
from config import Config
from steam_api_handler import SteamAPIHandler
from steam_top_sellers_scraper import SteamTopSellersScraper
from data_processor import DataProcessor


def main(api_key, steam_id, top_n=10):
    config = Config(api_key, steam_id)
    steam_api_handler = SteamAPIHandler(config)
    scraper = SteamTopSellersScraper()

    # Fetch data
    owned_games_df = steam_api_handler.fetch_owned_games()
    all_games_df = steam_api_handler.fetch_all_games()
    top_sellers_df = scraper.scrape_top_sellers(top_n=top_n)

    # Process data
    processor = DataProcessor(owned_games_df, all_games_df, top_sellers_df)
    recommended_games = processor.process()

    # Export recommended top games not owned by user to CSV
    recommended_games.to_csv("recommended_games.csv", index=False)
    print(f"Exported recommended top {top_n} games to 'recommended_games.csv'.")


if __name__ == "__main__":
    # Load environment variables
    dotenv.load_dotenv()

    STEAM_API_KEY = os.getenv("STEAM_API_KEY")
    STEAM_ID = os.getenv("STEAM_ID")

    parser = argparse.ArgumentParser(
        description="Fetch top selling games on Steam not owned by the user."
    )
    parser.add_argument(
        '--top_n',
        type=int,
        default=10,
        help="Number of top selling games to fetch. Default is 10.",
    )

    args = parser.parse_args()

    main(STEAM_API_KEY, STEAM_ID, args.top_n)
