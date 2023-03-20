import grequests
import requests
from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import json
import time
import logging

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
        self.driver = driver.get(url)
        self.html = BeautifulSoup(driver.execute_script("return document.body.outerHTML;"), "lxml")
        print(self.html)
        self.gameplay_panel = self.html.find_all(class_="panel panel-bottom ng-scope browse")
        self.credits_panel = self.html.find_all(class_="credits ng-scope")
        self.features_panel = self.html.find_all(class_="panel panel-bottom game-classification ng-scope")
        self.identifiers: list = []

    def get_gameplay(self):
        """
        Returns tuple containing: num players, time duration, age limit, weight (complexity of the game)
        """
        pass

    def get_features(self):
        """
        Returns tuple containing: type, category, mechanism
        """
        pass

    def get_creators(self):
        """
        Returns tuple containing: designers and artists
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


if __name__ == "__main__":
    main()
