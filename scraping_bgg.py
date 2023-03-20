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
    def __init__(self, index, url: str, driver):
        driver.get(url)
        driver.implicitly_wait(20)
        self.index = index
        self.html = BeautifulSoup(driver.execute_script("return document.body.outerHTML;"), "lxml")
        self.gameplay_panel = self.html.find(class_="panel panel-bottom ng-scope")
        self.credits_panel = self.html.find(class_="credits ng-scope")
        self.features_panel = self.html.find(class_="panel panel-bottom game-classification ng-scope")
        self.title_panel = self.html.find(class_="game-header-title-info")
        self.identifiers: list = self.get_gameplay() #+ self.get_features() + self.get_creators()
        self._title = self.get_title()
        print(self._title)

    def get_title(self):
        """
        Returns title of the game
        """
        results_title = self.html.find(class_='expandable-body')
        results_text = results_title.text.strip().split()
        index = results_text.index('is')
        title = ''
        for i in range(index):
            title += f'{results_text[i]} '
        return title

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

    def __str__(self):
        """
        returns string representation of an instance
        :return:
        """
        return(f'{self.index} - {self._title} > \n   Num_players(from,to): {self.identifiers[0]}, '
               f'time_duration(from,to): {self.identifiers[1]}, age_boundary: > {self.identifiers[2]}, '
               f'weight: {self.identifiers[3]}')


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

    games: dict = {} # building a dictionary of Game-objects
    for index, url in enumerate(games_pages_urls[:1]):
        games[f"game_{index}"] = Game(index, url, driver)
        print(games[f"game_{index}"])
    driver.quit()


if __name__ == "__main__":
    main()
