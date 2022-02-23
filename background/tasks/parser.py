from datetime import datetime
from background.celery_app import app as celery_app
from background.celery_app import database_session
from schemas.dota_item import DotaItemHistory, DotaItemSteamHistory
from repository.dota import get_all_item_names, create_item_history, create_item_steam_history
from steam.core import Currency
from steam.steam_client import SteamClient
from steam.steam_market import SteamMarket

client = SteamClient(cookies={'steamLoginSecure': '76561198380578038%7C%7CB03490B37E984F8F9BCF0FA131D8841E4C25FA07'})


@celery_app.task(queue="steam_queue")
def prepare_dota_tasks() -> None:
    """Create parse task for every dota item in database"""
    for item_hash_name, item_id in get_all_item_names(database_session):
        pull_history.delay(item_hash_name, item_id)


@celery_app.task(queue="steam_queue")
def pull_history(item_hash_name: str, item_id: int) -> None:
    fetched_data = SteamMarket(client).fetch_price(item_hash_name=item_hash_name, game_id=570, currency=Currency.RUB)
    item_history = DotaItemHistory(**fetched_data, item_id=item_id)
    create_item_history(database_session, item_history)

    celery_app.send_task(
        name="update_service_price",
        queue="items_base_queue",
        kwargs={
            "item_hash_name": item_hash_name,
            "game_id": 570,
            "price": item_history.price,
            "service": "STEAM"
        }
    )
    return


@celery_app.task(queue="steam_queue")
def pull_steam_history(item_hash_name: str, item_id: int):
    history = SteamMarket(client).fetch_history(item_hash_name)
    history_prices = history.get("prices")
    for date, price, volume in history_prices:
        date = date.split(": ")[0]
        date = datetime.strptime(date, "%b %d %Y %H")
        history_item = DotaItemSteamHistory(
            price=round(price, 2),
            item_id=item_id,
            volume=int(volume),
            date=date
        )
        create_item_steam_history(database_session, history_item)
    return
