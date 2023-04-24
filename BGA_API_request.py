from urllib.request import urlopen
import urllib.parse
import json

with open("BGG_configuration.json", "r") as f:
    config = json.load(f)

url_base_api = config['scraping']["URL_BASE_API"]
api_client_id = config['scraping']["API_CLIENT_ID"]

game_name_list = ['Brass: Birmingham', 'Pandemic Legacy: Season 1', 'Gloomhaven']  # for tuning


def get_game_bga_id(game_name):
    """
    Receives game_name and returns game_id from "Board Game Atlas" (API) site
    """
    url_game = f'{url_base_api}search?name={game_name}&client_id={api_client_id}'

    with urlopen(url_game) as url:
        data = json.load(url)

    return data["games"][0]["id"]


def get_prices_api(game_name):
    """
    Receives the game_name.
    Gets the game prices in all the US board game shops.
    Checks if the game is currently available in the shop and
    returns the list of dictionaries (one dictionary for each shop)
    with info on: store name and game price
    """
    game_encode = urllib.parse.quote_plus(game_name)  # url-encodes the game name
    game_id = get_game_bga_id(game_encode)
    url = f'{url_base_api}game/prices?game_id={game_id}&client_id={api_client_id}'
    with urlopen(url) as url:
        data = json.load(url)

    sellers: list = []
    prices: list = []

    for item in data["gameWithPrices"]["us"]:
        if item["in_stock"] is True and item["store_name"] not in sellers:
            sellers.append(item["store_name"])
            prices.append(item["price"])

    return {"sellers": tuple(sellers), "prices": tuple(prices)}
