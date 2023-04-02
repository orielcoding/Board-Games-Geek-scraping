import requests
from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import json
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


def get_html(url: str, driver):
    driver.get(url)
    return BeautifulSoup(driver.execute_script("return document.body.outerHTML;"), "lxml")


class Game:
    def __init__(self, url: str, driver):
        self.html: BeautifulSoup = get_html(url, driver)
        self.html_stats: BeautifulSoup = get_html(f"{url}/stats", driver)
        self.gameplay_panel = self.html.find(class_="panel panel-bottom ng-scope")
        self.credits_panel = self.html.find(class_="credits ng-scope")
        self.features_panel = self.html.find(class_="panel panel-bottom game-classification ng-scope")
        self.features = self.get_features()
        self.info: dict = self.get_title() | self.get_gameplay() | self.features | self.get_creators() | self.get_stats()

    def get_title(self) -> dict:
        """
        Returns dictionary containing game title and release year
        """
        html = self.html.find_all(class_="game-header-title-info")
        text_list = html[1].text.strip().split()
        game_title: str = ""
        game_year: int = None
        for item in text_list:
            if item[0] == '(' and item[5] == ')':
                game_year = int(item[1:-1])
                break
            else:
                game_title += f"{item} "

        return {"game_title": game_title, "game_year": game_year}

    def get_gameplay(self) -> dict:
        """
        Returns dictionary containing: num players, time duration, age limit, weight (complexity of the game)
        """
        gameplay_items = self.gameplay_panel.find_all(class_="gameplay-item")

        num_pattern = gameplay_items[0].find_all('span', class_='ng-binding ng-scope')
        if len(num_pattern) > 1:
            num_players = tuple([int(num_pattern[0].text.strip()), int(num_pattern[1].text.strip()[1:])])
        else:
            num_players = tuple([int(num_pattern[0].text.strip())])

        time_pattern = gameplay_items[1].find_all('span', class_='ng-binding ng-scope')

        if len(time_pattern) > 1:
            time_duration = tuple([int(time_pattern[0].text.strip()), int(time_pattern[1].text.strip()[1:])])
        else:
            time_duration = tuple([int(time_pattern[0].text.strip())])

        age_limit: int = int(re.search(r"[0-9]*(?=\+)", str(gameplay_items[2])).group())
        # age_limit = 0
        weight: float = float(re.search(r"[0-5]\.[0-9]{2}", str(gameplay_items[3])).group())
        # weight = 0
        return {"num_players": num_players, "time_duration": time_duration, "age_limit": age_limit, "weight": weight}

    def get_features(self) -> dict:
        """
        Returns dictionary containing: type, category, mechanism
        """
        features_items = self.features_panel.find_all(class_="feature ng-scope")

        game_type: tuple = tuple(i.string for i in features_items[0].find_all('a', {'class': 'ng-binding'}))

        category: tuple = tuple([i.get('title') for i in features_items[1].find_all('a', {'class': 'ng-binding'})[:-1]])

        mechanism: tuple = tuple(
            [i.get('title') for i in features_items[2].find_all('a', {'class': 'ng-binding'})[:-1]])

        reimplements = tuple([i.get('title') for i in features_items[-1].find_all('a', {'class': 'ng-binding'})[:-1]])

        return {"game_type": game_type, "category": category, "mechanism": mechanism, "reimplements": reimplements}

    def get_creators(self) -> dict:
        """
        Returns dictionary containing: designers and artists
        """
        creators_items = self.credits_panel.find_all(action="geekitemctrl.showFullCredits")

        designers_line = creators_items[0].find_all(attrs={"title": True})
        designers: tuple = tuple([designer.get('title') for designer in designers_line])

        artists_line = creators_items[1].find_all(attrs={"title": True})
        artists: tuple = tuple([artist.get('title') for artist in artists_line])

        return {"designers": designers, "artists": artists}

    def get_stats(self) -> dict:
        """
        Returns dictionary containing statistical info about the games.
        """
        html = self.html_stats.find_all(class_="outline-item-description")
        aggregate_rating = html[0].text.strip()
        review_count = html[1].text.strip()
        num_comments = html[4].text.strip()
        page_views = html[6].text.strip()
        overall_rank = int(re.match('[0-9]+', html[7].text.strip()).group())

        num_types: int = len(self.features["game_type"])
        types_rank: list = []
        for index in range(num_types):
            types_rank.append(int(re.match('[0-9]+', html[8 + index].text.strip()).group()))
        all_time_plays = int(html[9 + num_types - 1].text.strip())
        this_month_plays = int(html[10 + num_types - 1].text.strip())
        num_own = int(html[11 + num_types - 1].text.strip())
        num_wishlist = int(html[15 + num_types - 1].text.strip())

        return {"aggregate_rating": aggregate_rating, "review_count": review_count, "num_comments": num_comments,
                "page_views": page_views, "overall_rank": overall_rank, "all_time_plays": all_time_plays,
                "this_month_plays": this_month_plays,
                "num_own": num_own, "num_wishlist": num_wishlist}

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

    games_pages_urls: list = []
    for index in range(config["NUM_GAMES_TO_COLLECT"] // config["NUM_GAMES_PER_PAGE"]):
        games_pages_urls.append(get_urls(index))

    games: dict = {}
    for list_index, lst in enumerate(games_pages_urls):
        for index, url in enumerate(lst):
            games[f"game_{list_index * 100 + index}"]: Game = Game(url, driver)


if __name__ == "__main__":
    main()
