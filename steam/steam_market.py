from steam.core import COMMUNITY_URL, Currency
from steam.steam_client import SteamClient


class SteamMarket:
    """Base class to pull data from steam

    Methods:
        fetch_price - return current item price
        fetch_history - return price history of item
    """

    def __init__(self, client: SteamClient):
        self.client = client

    @staticmethod
    def _get_price_rub(price: str):
        return float(price.split()[0].replace(",", "."))

    @staticmethod
    def _parse_price(response: dict, currency: Currency = Currency.RUB) -> dict:
        if currency != Currency.RUB:
            raise Exception("We not support this currency yet")
        price = SteamMarket._get_price_rub(response.get("lowest_price"))
        median_price = response.get("median_price", None)
        median_price = SteamMarket._get_price_rub(median_price) if median_price else None
        return {
            "price": price,
            "median_price": median_price,
            "volume": response.get("volume", 0),
            "currency": currency
        }

    def fetch_price(self, item_hash_name: str, game_id: int = 570, currency: Currency = Currency.RUB) -> dict:
        """Function will fetch current price of item on steam market

        :param item_hash_name: full name of item at steam market
        :param game_id: item game id
        :param currency: id of currency in steam DB, by default RUB
        :return: pulled data
        """
        url = f"{COMMUNITY_URL}/market/priceoverview/"
        params = {
            "country": "RU",
            'currency': currency.value,
            'appid': game_id,
            'market_hash_name': item_hash_name
        }
        response = self.client.get(url, params=params)
        return SteamMarket._parse_price(response.json())

    def fetch_history(self, item_hash_name: str, game_id: int = 570) -> dict:
        """Function will fetch price history of item on steam market

        Currency of returned price will be default currency of account.

        :param item_hash_name: full name of item at steam market
        :param game_id: item game id
        :return: pulled data
        """
        url = f"{COMMUNITY_URL}/market/pricehistory/"
        params = {
            "country": "RU",
            'appid': game_id,
            'market_hash_name': item_hash_name
        }
        response = self.client.get(url, cookies=True, params=params)
        if response.status_code != 200:
            raise Exception(f"Received {response.status_code} http code from {response.url}")
        return response.json()
