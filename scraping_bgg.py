import grequests
import requests
from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import json
import time
import logging
import re

with open("BGG_configuration.json", "r") as f:
    config = json.load(f)


def get_urls(page_num: int) -> list[str]:
    """
    This func sends a request to a html page that contain multiple desired urls and returns a list of them
    """
    result = requests.get(config["URL"] + f"{page_num}", headers=config["HEADERS"])

    doc = BeautifulSoup(result.text, "lxml")

    # class is identifier to find where the links to games pages are located inside the text
    tags = doc.find_all(class_="collection_objectname browse")

    return [config["DOMAIN"] + tag.find(attrs={"href": True}).get("href") for tag in tags]


class Game:
    def __init__(self, url: str, driver):
        self.html: BeautifulSoup = self.get_html(url, driver)
        self.gameplay_panel = self.html.find(class_="panel panel-bottom ng-scope")
        self.credits_panel = self.html.find(class_="credits ng-scope")
        self.features_panel = self.html.find(class_="panel panel-bottom game-classification ng-scope")
        self.info: dict = self.get_gameplay() | self.get_features() | self.get_creators()


    def get_html(self, url: str, driver):
        driver.get(url)
        return BeautifulSoup(driver.execute_script("return document.body.outerHTML;"), "lxml")

    def get_gameplay(self) -> dict:
        """
        Returns list containing: num players, time duration, age limit, weight (complexity of the game)
        """
        gameplay_items = self.gameplay_panel.find_all(class_="gameplay-item")

        num_pattern = gameplay_items[0].find_all('span', class_= 'ng-binding ng-scope')
        if len(num_pattern)>1:
            num_players = tuple([int(num_pattern[0].text.strip()), int(num_pattern[1].text.strip()[1:])])
        else:
            num_players = tuple([int(num_pattern[0].text.strip())])

        time_pattern = gameplay_items[1].find_all('span', class_= 'ng-binding ng-scope')

        if len(time_pattern)>1:
            time_duration = tuple([int(time_pattern[0].text.strip()), int(time_pattern[1].text.strip()[1:])])
        else:
            time_duration = tuple([int(time_pattern[0].text.strip())])

        age_limit: int = int(re.search(r"[0-5]*(?=\+)", str(gameplay_items[2])).group())

        weight: float = float(re.search(r"[0-5]\.[0-9]{2}", str(gameplay_items[3])).group())

        return {"num_players": num_players, "time_duration": time_duration, "age_limit": age_limit, "weight": weight}

    def get_features(self) -> dict:
        """
        Returns list containing: type, category, mechanism
        """
        features_items = self.features_panel.find_all(class_="feature ng-scope")

        game_type: str = features_items[0].find('a', {'class': 'ng-binding'}).string

        category: tuple = tuple([i.get('title') for i in features_items[1].find_all('a', {'class': 'ng-binding'})[:-1]])

        mechanism: tuple = tuple([i.get('title') for i in features_items[2].find_all('a', {'class': 'ng-binding'})[:-1]])

        reimplements = tuple([i.get('title') for i in features_items[-1].find_all('a', {'class': 'ng-binding'})[:-1]])

        return {"game_type": game_type, "category": category, "mechanism": mechanism, "reimplements": reimplements}

    def get_creators(self) -> dict:
        """
        Returns list containing: designers and artists
        """
        creators_items = self.credits_panel.find_all(action="geekitemctrl.showFullCredits")

        designers_line = creators_items[0].find_all(attrs={"title": True})
        designers: tuple = tuple([designer.get('title') for designer in designers_line])

        artists_line = creators_items[1].find_all(attrs={"title": True})
        artists: tuple = tuple([artist.get('title') for artist in artists_line])

        return {"designers": designers, "artists": artists}


    def get_info(self) -> dict:
        """
        Returns all the info of a game
        """
        return self.info


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument(f'user-agent={config["HEADERS"]["User-Agent"]}')
    driver = Chrome(options=options)
    driver.implicitly_wait(5)

    games_pages_urls: list[str] = []
    # for index in range(config["NUM_GAMES_TO_COLLECT"] // config["NUM_GAMES_PER_PAGE"]):
    for index in range(2):
        games_pages_urls += get_urls(index)

    games: dict = {}
    for index, url in enumerate(games_pages_urls[52:100]):
        games[f"game_{index}"]: Game = Game(url, driver)
        print(games[f"game_{index}"].get_info())


if __name__ == "__main__":
    main()
