from background.celery_app import app

from steam.steam_client import SteamClient
from steam.steam_market import SteamMarket

client = SteamClient(cookies={'steamLoginSecure': '76561198380578038%7C%7CFFD9F1531D2D11B4BF6E69BF87B0FBEBA7945D2B'})


@app.task(queue="steam_queue")
def pull_history(item_hash_name: str) -> dict:
    return SteamMarket(client).fetch_history(item_hash_name)
