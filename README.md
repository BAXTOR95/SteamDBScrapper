# Steam Top Sellers Scraper

This project is designed to help Steam users discover new games by identifying top-selling games they do not currently own. It utilizes the Steam API to fetch a user's owned games and Selenium WebDriver to scrape current top-selling games from the Steam store. The results are processed and provided in a CSV file, making it easy to view which popular games could be your next purchase.

## Features

- **User-specific game recommendations**: Compares user's owned games with the Steam top sellers to recommend new games.
- **Dynamic web scraping**: Uses Selenium to dynamically load and scrape the Steam Top Sellers page.
- **CLI support**: Allows users to specify the number of games they want to fetch via command-line arguments.
- **Easy integration**: Easily extendable codebase with clear class-based separation for different functionalities.

## Prerequisites

Before you can use this project, you need to have the following installed:

- Python 3.6 or higher
- Selenium WebDriver
- ChromeDriver (compatible with your Chrome version)
- `requests` and `pandas` Python libraries

## Installation

Follow these steps to set up the project environment:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/BAXTOR95/SteamTopSellersScraper.git
   cd SteamTopSellersScraper
   ```

2. **Set up a Python Virtual Environment (Optional but recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Required Python Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download ChromeDriver**

   Make sure you download the version of ChromeDriver that matches your version of Chrome. Place it in a directory accessible by your system's PATH, or modify the script to point to its location.

5. **Setting up .env file**

    Make sure you create a .env on the root of the project with the following content:

    ```plaintext
    STEAM_API_KEY=YOUR_API_KEY
    STEAM_ID=YOUR_STEAM_ID
    ```

## Usage

To use the script, you need your Steam API key and Steam ID. You can obtain your API key from [Steam's Developer Portal](https://steamcommunity.com/dev/apikey).

1. **Basic Usage**

   Navigate to the script's directory and run:

   ```bash
   python main.py --top_n 50
   ```

   Adjust `--top_n` to control how many top-selling games to fetch and compare.

2. **Parameters**

   - `--top_n`: (Optional) Specifies the number of top-selling games to fetch (default is 10).

3. **Output**

   The script outputs a file named `recommended_games.csv` in the current directory. This file lists the top-selling games not currently owned by the user, formatted as:

   ```csv
   appid,title,url
   123456,Game Title,https://store.steampowered.com/app/123456/
   ...
   ```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@BAXTOR95](https://twitter.com/BAXTOR95) - <brian.arriaga@gmail.com>

Project Link: [https://github.com/BAXTOR95/SteamTopSellersScraper](https://github.com/BAXTOR95/SteamTopSellersScraper)
