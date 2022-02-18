from background.celery_app import app as celery_app
from db import get_session
from schemas.dota_item import SteamDotaItemHistoryRUB, DotaItemHistory
from repository.dota import get_all_item_names, create_item_history
from steam.core import Currency
from steam.steam_client import SteamClient
from steam.steam_market import SteamMarket

client = SteamClient(cookies={'steamLoginSecure': '76561198380578038%7C%7CFFD9F1531D2D11B4BF6E69BF87B0FBEBA7945D2B'})


@celery_app.task(queue="steam_queue")
def prepare_dota_tasks() -> None:
    """Create parse task for every dota item in database"""
    for item_hash_name, item_id in get_all_item_names(next(get_session())):
        pull_history.delay(item_hash_name, item_id)


@celery_app.task(queue="steam_queue")
def pull_history(item_hash_name: str, item_id: int) -> None:
    fetched_data = SteamMarket(client).fetch_price(item_hash_name=item_hash_name, game_id=570, currency=Currency.RUB)
    item_history = DotaItemHistory(**fetched_data, item_id=item_id)
    create_item_history(next(get_session()), item_history)
    return
