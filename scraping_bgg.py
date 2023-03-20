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

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument(f'user-agent={config["HEADERS"]["User-Agent"]}')

    driver = Chrome(options=options)
    games_pages_urls: list[str] = []

    # for index in range(config["NUM_GAMES_TO_COLLECT"] // config["NUM_GAMES_PER_PAGE"]):
    for index in range(2):
        games_pages_urls += get_urls(index)

    for url in games_pages_urls[:1]:
        driver.get(url)
        # HTML from `<body>`
        html = driver.execute_script("return document.body.outerHTML;")
        print(html)


if __name__ == "__main__":
    main()
