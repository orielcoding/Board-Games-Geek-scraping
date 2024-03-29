import requests
from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import json
import argparse
import logging
import re
import saving_to_db
import BGA_API_request
import create_db
from logging_decorator import exception, create_logger


with open("BGG_configuration.json", "r") as f:
    config = json.load(f)

logger = create_logger()


@exception
def get_urls(page_num: int, quantity: int = config['scraping']["NUM_GAMES_PER_PAGE"]) -> list[str]:
    """
    This func sends a request to a html page that contain multiple desired urls and returns a list of them
    """
    result = requests.get(config['scraping']["URL"] + f"{page_num}", headers=config['scraping']["HEADERS"])

    doc = BeautifulSoup(result.text, "lxml")

    # class is identifier to find where the links to games pages are located inside the text
    tags = doc.find_all(class_="collection_objectname browse")

    return [config['scraping']["DOMAIN"] + tag.find(attrs={"href": True}).get("href") for tag in tags[0:quantity]]


@exception
def get_html_body(url: str, driver):
    driver.get(url)
    return BeautifulSoup(driver.execute_script("return document.body.outerHTML;"), "lxml")


@exception
def get_html_head(url: str, driver):
    driver.get(url)
    return BeautifulSoup(driver.execute_script("return document.head.outerHTML;"), "lxml")


class Game:
    def __init__(self, url: str, driver, options):
        self.options = options
        self.html: BeautifulSoup = get_html_body(url, driver)
        self.html_head: BeautifulSoup = get_html_head(url, driver)
        self.html_stats: BeautifulSoup = get_html_body(f"{url}/stats", driver)
        self.gameplay_panel = self.html.find(class_="panel panel-bottom ng-scope")
        self.credits_panel = self.html.find(class_="credits ng-scope")
        self.features_panel = self.html.find(class_="panel panel-bottom game-classification ng-scope")
        self.features = self.get_features()
        if len(self.options) == 0 or 'a' in self.options:
            self.info: dict = self.get_title() | self.get_gameplay() | self.get_features() \
                              | self.get_creators() | self.get_stats() | self.get_site_id() | self.get_prices()
        else:
            self.info: dict = self.get_title()
            if 'g' in self.options: self.info = self.info | self.get_gameplay()
            if 'f' in self.options: self.info = self.info | self.get_features()
            if 'c' in self.options: self.info = self.info | self.get_creators()
            if 's' in self.options: self.info = self.info | self.get_stats()
            if 'a' in self.options: self.info = self.info | self.get_prices()

    @exception
    def get_site_id(self):
        html = self.html_head.find("link")
        game_site_id: int = int(re.search(r'\d+', str(html)).group())
        return {"game_site_id": game_site_id}

    @exception
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

    @exception
    def get_gameplay(self) -> dict:
        """
        Returns dictionary containing: num players, time duration, age limit, weight (complexity of the game)
        """
        gameplay_items = self.gameplay_panel.find_all(class_="gameplay-item")

        num_pattern = gameplay_items[0].find_all('span', class_='ng-binding ng-scope')
        if len(num_pattern) > 1:
            min_n_players = int(num_pattern[0].text.strip())
            max_n_players = int(num_pattern[1].text.strip()[1:])
        else:
            min_n_players = int(num_pattern[0].text.strip())
            max_n_players = None

        time_pattern = gameplay_items[1].find_all('span', class_='ng-binding ng-scope')

        if len(time_pattern) > 1:
            min_time = int(time_pattern[0].text.strip())
            max_time = int(time_pattern[1].text.strip()[1:])
        else:
            min_time = int(time_pattern[0].text.strip())
            max_time = None

        age_limit: int = int(re.search(r"[0-9]*(?=\+)", str(gameplay_items[2])).group())

        weight: float = float(re.search(r"[0-5]\.[0-9]{2}", str(gameplay_items[3])).group())

        return {"min_n_players": min_n_players, "max_n_players": max_n_players, "min_time": min_time,
                "max_time": max_time, "age_limit": age_limit, "weight": weight}

    @exception
    def get_features(self) -> dict:
        """
        Returns dictionary containing: type, category, mechanism
        """
        features_items = self.features_panel.find_all(class_="feature ng-scope")

        game_type: tuple = tuple(i.string for i in features_items[0].find_all('a', {'class': 'ng-binding'}))

        category: tuple = tuple([i.get('title') for i in features_items[1].find_all('a', {'class': 'ng-binding'})[:-1]])

        mechanism: tuple = tuple(
            [i.get('title') for i in features_items[2].find_all('a', {'class': 'ng-binding'})[:-1]])

        return {"game_type": game_type, "category": category, "mechanism": mechanism}

    @exception
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

    @exception
    def get_stats(self) -> dict:
        """
        Returns dictionary containing statistical info about the games.
        """
        html = self.html_stats.find_all(class_="outline-item-description")
        aggregate_rating = float(html[0].text.strip())
        review_count = int(html[1].text.strip().replace(',', ''))
        num_comments = int(html[4].text.strip().replace(',', ''))
        page_views = int(html[6].text.strip().replace(',', ''))
        overall_rank = int(re.match('[0-9]+', html[7].text.strip()).group())

        num_types: int = len(self.features["game_type"])
        types_rank: int = int(re.match('[0-9]+', html[8].text.strip()).group())
        all_time_plays = int((html[9 + num_types - 1].text.strip().replace(',', '')))
        this_month_plays = int(html[10 + num_types - 1].text.strip().replace(',', ''))
        num_own = int(html[11 + num_types - 1].text.strip().replace(',', ''))
        num_wishlist = int(html[15 + num_types - 1].text.strip().replace(',', ''))

        return {"aggregate_rating": aggregate_rating, "overall_rank": overall_rank, "types_rank": types_rank,
                "num_comments": num_comments, "page_views": page_views, "all_time_plays": all_time_plays,
                "this_month_plays": this_month_plays, "num_own": num_own,
                "num_wishlist": num_wishlist, "review_count": review_count}

    @exception
    def get_prices(self) -> dict:
        """
        Returns dictionary containing the 'us' shops, where the game is sold and it's prices
        """
        game_name = self.get_title()["game_title"]
        return BGA_API_request.get_prices_api(game_name)

    @exception
    def get_info(self) -> dict:
        """
        Returns all the info of a game
        """
        return self.info

    def __setitem__(self, key, value):
        self.info[key] = value


@exception
def save_to_database(games: dict, include_api: bool = False) -> None:
    """
    This function is called to save games into databases. This function use the saving_to_db class.
    """
    db_tables = saving_to_db.connect_to_db_tables()

    # independent tables:

    game = [[v.get_info()[key] for key in ['game_site_id', 'game_title']] for v in
            games.values()]
    saving_to_db.data_to_db(db_tables['game'], game, normalized=True, unique_column='site_id')
    logger.info(f"RESULT: populated game table")

    artists = [[v.get_info()[key] for key in ['artists']] for v in games.values()]
    saving_to_db.data_to_db(db_tables['artists'], artists, unique_column='artist_name')
    logger.info(f"RESULT: populated artists table")

    categories = [[v.get_info()[key] for key in ['category']] for v in games.values()]
    saving_to_db.data_to_db(db_tables['categories'], categories, unique_column='category')
    logger.info(f"RESULT: populated categories table")

    designers = [[v.get_info()[key] for key in ['designers']] for v in games.values()]
    saving_to_db.data_to_db(db_tables['designers'], designers, unique_column='designer_name')
    logger.info(f"RESULT: populated designers table")

    mechanics = [[v.get_info()[key] for key in ['mechanism']] for v in games.values()]
    saving_to_db.data_to_db(db_tables['mechanics'], mechanics, unique_column='mechanic')
    logger.info(f"RESULT: populated mechanics table")

    types = [[v.get_info()[key] for key in ['game_type']] for v in games.values()]
    saving_to_db.data_to_db(db_tables['types'], types, unique_column='type')
    logger.info(f"RESULT: populated types table")

    game_stats = [[v.get_info()[key] for key in ['game_site_id'] + list(v.get_stats().keys())] for v in games.values()]
    saving_to_db.data_to_db(db_tables['game_stats'], game_stats, normalized=True)
    logger.info(f"RESULT: populated game_stats table")

    # related tables by 1 foreign key:
    general_info = [[v.get_info()[key] for key in ['game_site_id', 'game_type', 'min_n_players', 'max_n_players',
                                                   'weight', 'game_year', 'min_time', 'max_time', 'age_limit']] for v in
                    games.values()]
    saving_to_db.data_to_db(db_tables['general_info'], general_info, inherit_from=[db_tables['types']],
                            match_fk_col=['type_id'], match_val_col=['type'])
    logger.info(f"RESULT: populated general_info table")

    # related tables by 2 foreign keys:

    game_artists = [[v.get_info()[key] for key in ['game_site_id', 'artists', ]] for v in games.values()]
    saving_to_db.data_to_db(db_tables['game_artists'], game_artists, inherit_from=[db_tables['artists']],
                            match_fk_col=['artist_id'], match_val_col=['artist_name'])
    logger.info(f"RESULT: populated game_artists table")

    game_categories = [[v.get_info()[key] for key in ['game_site_id', 'category']] for v in games.values()]
    saving_to_db.data_to_db(db_tables['game_category'], game_categories, inherit_from=[db_tables['categories']],
                            match_fk_col=['category_id'], match_val_col=['category'])
    logger.info(f"RESULT: populated game_categories table")

    game_designers = [[v.get_info()[key] for key in ['game_site_id', 'designers']] for v in games.values()]
    saving_to_db.data_to_db(db_tables['game_designers'], game_designers, inherit_from=[db_tables['designers']],
                            match_fk_col=['designer_id'], match_val_col=['designer_name'])
    logger.info(f"RESULT: populated game_designers table")

    game_mechanics = [[v.get_info()[key] for key in ['game_site_id', 'mechanism']] for v in games.values()]
    saving_to_db.data_to_db(db_tables['game_mechanics'], game_mechanics, inherit_from=[db_tables['mechanics']],
                            match_fk_col=['mechanic_id'], match_val_col=['mechanic'])
    logger.info(f"RESULT: populated game_mechanics table")

    if include_api:
        sellers = [[v.get_info()[key] for key in ['sellers']] for v in games.values()]
        saving_to_db.data_to_db(db_tables['sellers'], sellers, unique_column='seller_id')
        logger.info(f"RESULT: populated sellers table")

        game_sellers = [[v.get_info()[key] for key in ['game_site_id', 'sellers', 'prices']] for v in games.values()]
        # normalizing manually instead with built function because need to have specific sets of seller-price together.
        normalized_rows = []
        for i in game_sellers:
            for j in range(len(i[1])):
                normalized_rows.append([i[0], i[1][j], i[2][j]])
        saving_to_db.data_to_db(db_tables['game_sellers'], normalized_rows, normalized=True,
                                inherit_from=[db_tables['sellers']], match_fk_col=['seller_id'],
                                match_val_col=['seller_name'])
        logger.info(f"RESULT: populated game_sellers table")


@exception
def bgg_scrape_games(scraping_options: list, count: int) -> dict:
    """
    This function scrape data. specifically, it scrapes data from bgg site.
    The argument controls the scraping options from bgg.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument(f'user-agent={config["scraping"]["HEADERS"]["User-Agent"]}')
    driver = Chrome(options=options)
    driver.implicitly_wait(2)

    games_pages_urls: list = []
    for index in range(count // config['scraping']["NUM_GAMES_PER_PAGE"]):
        games_pages_urls.append(get_urls(index))

    games_pages_urls.append(get_urls(count // config['scraping']["NUM_GAMES_PER_PAGE"],
                                     count % config['scraping']["NUM_GAMES_PER_PAGE"]))

    games: dict = {}
    for list_index, lst in enumerate(games_pages_urls):
        for index, url in enumerate(lst):
            games[f"game_{list_index * 100 + index}"]: Game = Game(url, driver, scraping_options)
            info_to_print = games[f"game_{list_index * 100 + index}"].get_site_id()
            print(info_to_print)
            logger.info(f"RESULT: scraped game with {info_to_print}")
    return games


@exception
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num_games', type=int, help='specifies number of pages to scrap')
    parser.add_argument('-s', '--stats', action='store_true', help='limits data collection to stats')
    parser.add_argument('-c', '--creators', action='store_true', help='limits data collection to info on creators')
    parser.add_argument('-g', '--gameplay', action='store_true', help='limits data collection to info on gameplay')
    parser.add_argument('-f', '--features', action='store_true', help='limits data collection to info about features')
    parser.add_argument('-d', '--database', action='store_true', help='to save the info into sql database')
    parser.add_argument('-a', '--api', action='store_true', help='to also get the prices from BGA API')

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
    if args.api: cli_options.append('a')

    if args.num_games:
        count = args.num_games
    else:
        count = config['scraping']["NUM_GAMES_TO_COLLECT"]

    # scraping games
    games = bgg_scrape_games(cli_options, count)

    # creating db if required
    create_db.main()
    # saving game instances information into database
    save_to_database(games, include_api=args.api)

    if args.database:
        # creating db if required
        create_db.main()
        # saving game instances information into database
        save_to_database(games, include_api=args.api)


if __name__ == "__main__":
    main()
