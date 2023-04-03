import requests
from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import json
import argparse
# from pathlib import Path
# import time
import logging
from functools import wraps
import re
import saving_to_db

with open("BGG_configuration.json", "r") as f:
    config = json.load(f)


def create_logger():
    # creates a logger object
    logger = logging.getLogger('exc_logger')
    logger.setLevel(logging.INFO)

    # creates a file to store all the logged exceptions
    # ? need to put the file name to json ??
    logfile = logging.FileHandler('bgg_exception.log')
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)
    return logger


logger = create_logger()


def exception(logger):
    # logger is the logging object
    # exception is the decorator objects that logs every exception into log file
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                issue = "exception in " + func.__name__ + "\n"
                issue = issue + "-------------------------\
                ----------------------------------------------\n"
                logger.exception(issue)
            raise
        return wrapper
    return decorator


@exception(logger)
def get_urls(page_num: int, quantity: int = config["NUM_GAMES_PER_PAGE"]) -> list[str]:
    """
    This func sends a request to a html page that contain multiple desired urls and returns a list of them
    """
    result = requests.get(config["URL"] + f"{page_num}", headers=config["HEADERS"])

    doc = BeautifulSoup(result.text, "lxml")

    # class is identifier to find where the links to games pages are located inside the text
    tags = doc.find_all(class_="collection_objectname browse")

    return [config["DOMAIN"] + tag.find(attrs={"href": True}).get("href") for tag in tags[0:quantity]]


@exception(logger)
def get_html(url: str, driver):
    driver.get(url)
    return BeautifulSoup(driver.execute_script("return document.body.outerHTML;"), "lxml")


class Game:
    def __init__(self, url: str, driver, options):
        self.options = options
        self.html: BeautifulSoup = self.get_html(url, driver)
        self.html_stats: BeautifulSoup = self.get_html(f"{url}/stats", driver)
        self.gameplay_panel = self.html.find(class_="panel panel-bottom ng-scope")
        self.credits_panel = self.html.find(class_="credits ng-scope")
        self.features_panel = self.html.find(class_="panel panel-bottom game-classification ng-scope")
        self.features = self.get_features()
        if len(self.options) == 0:
            self.info: dict = self.get_title() | self.get_gameplay() | self.get_features() \
                              | self.get_creators() | self.get_stats()
        else:
            self.info: dict = self.get_title()
            if 'g' in self.options: self.info = self.info | self.get_gameplay()
            if 'f' in self.options: self.info = self.info | self.get_features()
            if 'c' in self.options: self.info = self.info | self.get_creators()
            if 's' in self.options: self.info = self.info | self.get_stats()

    @exception(logger)
    def get_title(self) -> dict:
        """
        Returns dictionary containing game title and release year
        """
        html = self.html.find_all(class_="game-header-title-info")
        text_list = html[1].text.strip().split()
        game_title: str = ""
        game_year: int = 0
        for item in text_list:
            if item[0] == '(' and item[5] == ')':
                game_year = int(item[1:-1])
                break
            else:
                game_title += f"{item} "

        return {"game_title": game_title, "game_year": game_year}

    @exception(logger)
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

    @exception(logger)
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

    @exception(logger)
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

    @exception(logger)
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
        all_time_plays = int((html[9 + num_types - 1].text.strip().replace(',', '')))
        this_month_plays = int(html[10 + num_types - 1].text.strip().replace(',', ''))
        num_own = int(html[11 + num_types - 1].text.strip().replace(',', ''))
        num_wishlist = int(html[15 + num_types - 1].text.strip().replace(',', ''))

        return {"aggregate_rating": aggregate_rating, "overall_rank": overall_rank, "types_rank": types_rank,
                "num_comments": num_comments, "page_views": page_views, "all_time_plays": all_time_plays,
                "this_month_plays": this_month_plays, "num_own": num_own,
                "num_wishlist": num_wishlist, "review_count": review_count}

    @exception(logger)
    def get_info(self) -> dict:
        """
        Returns all the info of a game
        """
        return self.info


@exception(logger)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num_games', type=int, help='specifies number of pages to scrap')
    parser.add_argument('-s', '--stats', action='store_true', help='limits data collection to stats')
    parser.add_argument('-c', '--creators', action='store_true', help='limits data collection to info on creators')
    parser.add_argument('-g', '--gameplay', action='store_true', help='limits data collection to info on gameplay')
    parser.add_argument('-f', '--features', action='store_true', help='limits data collection to info about features')
    parser.add_argument('-d', '--database', action='store_true', help='to save the info into sql database')

    args = parser.parse_args()

    """
    building list of options to be used as one more parameter for Game class, 
    the content of self.info will depend on it:
    """
    cli_options = []
    if args.stats: cli_options.append('s')
    if args.creators: cli_options.append('c')
    if args.gameplay: cli_options.append('g')
    if args.features: cli_options.append('f')

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument(f'user-agent={config["HEADERS"]["User-Agent"]}')
    driver = Chrome(options=options)
    driver.implicitly_wait(5)

    if args.num_games:
        count = args.num_games
    else:
        count = config["NUM_GAMES_TO_COLLECT"]

    games_pages_urls: list = []
    for index in range(count // config["NUM_GAMES_PER_PAGE"]):
        games_pages_urls.append(get_urls(index))

    games_pages_urls.append(get_urls(count // config["NUM_GAMES_PER_PAGE"], count % config["NUM_GAMES_PER_PAGE"]))

    games: dict = {}
    for list_index, lst in enumerate(games_pages_urls):
        for index, url in enumerate(lst):
            games[f"game_{list_index * 100 + index}"]: Game = Game(url, driver, cli_options)
            print(games[f"game_{index}"].get_info())
            if args.database:
                """
                writes the scraped data to database
                """
                pass

    db_tables = saving_to_db.connect_to_db_tables()

    obj_list_values = [v.get_info()['game_title'] for v in games.values()]
    saving_to_db.saving_independent_tables_info(db_tables['game'], obj_list_values, 'name')

    obj_list_values = [[v.get_info()['game_title']] + list(v.get_stats().values()) for v in games.values()]
    saving_to_db.saving_to_first_level_relational_tables(db_tables['game_stats'], obj_list_values, db_tables['game'])
    saving_to_db.describe_table(db_tables['game_stats'])


if __name__ == "__main__":
    main()
