import grequests
import requests
import re
import time
from bs4 import BeautifulSoup
import json
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


def main():
    games_pages_urls: list[str] = []
    for index in range(config["NUM_GAMES_TO_COLLECT"] // config["NUM_GAMES_PER_PAGE"]):
        print(len(games_pages_urls))
        games_pages_urls += get_urls(index)


if __name__ == "__main__":
    main()
