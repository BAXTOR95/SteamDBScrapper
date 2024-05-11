import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class SteamTopSellersScraper:
    def __init__(self, url="https://store.steampowered.com/search/?filter=topsellers"):
        self.url = url

    def scrape_top_sellers(self, top_n=100):
        # Set up Chrome WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(self.url)
        time.sleep(3)  # Allow some time for the page to load

        # Scroll to load more games
        last_height = driver.execute_script("return document.body.scrollHeight")
        while (
            len(driver.find_elements(By.CSS_SELECTOR, '#search_resultsRows > a'))
            < top_n
        ):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Allow time for more results to load

            # Break the loop if the page height does not increase
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Extract game titles and URLs
        game_elements = driver.find_elements(By.CSS_SELECTOR, '#search_resultsRows > a')
        top_sellers = []
        for game_element in game_elements[:top_n]:
            try:
                title = game_element.find_element(By.CSS_SELECTOR, '.title').text
                href = game_element.get_attribute('href')
                app_id = href.split('/')[4]
                top_sellers.append({'appid': int(app_id), 'title': title, 'url': href})
            except Exception as e:
                print(f"Error processing an element: {e}")

        driver.quit()
        return pd.DataFrame(top_sellers)
