from urllib.request import urlopen
import urllib.parse
import json
import re

with open("BGG_configuration.json", "r") as f:
    config = json.load(f)

url_base_api = config["URL_BASE_API"]
api_client_id = config["API_CLIENT_ID"]

game_name_list = ['Brass: Birmingham', 'Pandemic Legacy: Season 1', 'Gloomhaven'] # for tuning


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
    Gets the game prices in all the US board game shops.
    Checks if the game is currently available in the shop and
    returns the list of dictionaries (one dictionary for each shop)
    with info on: store name and game price
    """
    game_id = get_game_bga_id(game_name)
    url = f'{url_base_api}game/prices?game_id={game_id}&client_id={api_client_id}'
    print(url)
    with urlopen(url) as url:
        data = json.load(url)

    results: list = []
    shops: list = []

    for item in data["gameWithPrices"]["us"]:
        if item["in_stock"] is True and item["store_name"] not in shops:
            store_dict: dict = {"store_name": item["store_name"],
                                "price": item["price"]}
            shops.append(item["store_name"])
            results.append(store_dict)

    return results


for game in game_name_list:
    game_encode = urllib.parse.quote_plus(game) # url-encodes the game name
    print(game, get_prices_api(game_encode))
