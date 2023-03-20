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
        driver.get(url)
        self.html = BeautifulSoup(driver.execute_script("return document.body.outerHTML;"), "lxml")
        self.gameplay_panel = self.html.find(class_="panel panel-bottom ng-scope")
        self.credits_panel = self.html.find(class_="credits ng-scope")
        self.features_panel = self.html.find(class_="panel panel-bottom game-classification ng-scope")
        self.identifiers: list = self.get_gameplay() + self.get_features() + self.get_creators()

    def get_gameplay(self) -> list:
        """
        Returns list containing: num players, time duration, age limit, weight (complexity of the game)
        """
        gameplay_items = self.gameplay_panel.find_all(class_="gameplay-item")
        num_players_pattern = gameplay_items[0].find(class_="ng-scope ng-isolate-scope").find_all(
            class_="ng-binding ng-scope")
        min_players: int = int(re.search(r">[1-9]<", str(num_players_pattern[0])).group()[1])
        max_players: int = int(re.search(r">[1-9]<", str(num_players_pattern[1])).group()[1])
        num_players: tuple[int, int] = (min_players, max_players)

        time_pattern = gameplay_items[1].find_all(class_="ng-binding ng-scope")
        min_time: int = int(re.search(r">[0-9]*<", str(time_pattern[0])).group()[1:-1])
        max_time: int = int(re.search(r">([0-9]+)<", str(time_pattern[1])).group()[1:-1])
        time_duration: tuple[int, int] = (min_time, max_time)

        age_boundary: int = int(re.search(r"[0-5]*(?=\+)", str(gameplay_items[2])).group())

        weight: float = float(re.search(r"[0-5]\.[0-9]{2}", str(gameplay_items[3])).group())

        return [num_players, time_duration, age_boundary, weight]

    def get_features(self) -> list:
        """
        Returns list containing: type, category, mechanism
        """
        pass

    def get_creators(self) -> list:
        """
        Returns list containing: designers and artists
        """
        pass

    def get_info(self):
        """
        Returns all the info of a game
        """
        pass


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
    for index, url in enumerate(games_pages_urls[:1]):
        games[f"game_{index}"] = Game(url, driver)
        games[f"game_{index}"].get_gameplay()


if __name__ == "__main__":
    main()
