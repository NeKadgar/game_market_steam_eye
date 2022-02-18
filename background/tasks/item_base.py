from background.celery_app import app
from db import get_session

from repository.dota import create_item

from steam.steam_client import SteamClient
from steam.steam_market import SteamMarket
from schemas.dota_item import DotaItemCreate

client = SteamClient(cookies={'steamLoginSecure': '76561198380578038%7C%7CFFD9F1531D2D11B4BF6E69BF87B0FBEBA7945D2B'})


@app.task(name="update_steam_items", queue="base_steam_queue")
def update_steam_items(item_hash_name: str) -> None:
    """Will add new dota item to dota_item table to the next monitoring by parser

    Function return nothing, we care only if error raised.

    :param item_hash_name: steam name of item
    :return:
    """
    item = DotaItemCreate(name=item_hash_name)
    create_item(next(get_session()), item)
    return
